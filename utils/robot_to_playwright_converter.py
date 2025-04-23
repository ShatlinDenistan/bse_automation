import os
import re
import shutil
from pathlib import Path


class RobotToPlaywrightConverter:
    """Converts Robot Framework tests to Playwright tests"""

    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.robot_dir = os.path.join(base_dir, "robot")
        self.pos_dir = os.path.join(base_dir, "pos")
        self.pages_dir = os.path.join(base_dir, "pages")
        self.tests_dir = os.path.join(base_dir, "tests", "ui")

        # Ensure directories exist
        for directory in [self.pos_dir, self.pages_dir, self.tests_dir]:
            os.makedirs(directory, exist_ok=True)

    def convert_all(self):
        """Convert all Robot Framework files to Playwright"""
        # Convert OR files to PO files
        self._convert_or_files()

        # Convert KW files to Page files
        self._convert_kw_files()

        # Convert Test files to Playwright test files
        self._convert_test_files()

        # Update page_initializer.py with new pages
        self._update_page_initializer()

        return "Conversion completed successfully!"

    def _convert_or_files(self):
        """Convert OR files to PO files"""
        or_dir = os.path.join(self.robot_dir, "OR")

        for file_name in os.listdir(or_dir):
            if file_name.endswith(".robot"):
                robot_file_path = os.path.join(or_dir, file_name)

                # Generate PO file name (e.g., orSearch.robot -> search_po.py)
                base_name = file_name[2:-6].lower()  # Remove 'or' prefix and '.robot' suffix
                po_file_name = f"{base_name}_po.py"
                po_file_path = os.path.join(self.pos_dir, po_file_name)

                # Skip if file already exists
                if os.path.exists(po_file_path):
                    print(f"Skipping {po_file_name} as it already exists.")
                    continue

                print(f"Converting {file_name} to {po_file_name}")

                # Parse the Robot file to extract variables
                variables = self._extract_variables_from_robot(robot_file_path)

                # Generate the PO class content
                po_content = self._generate_po_class(base_name, variables)

                # Write the PO file
                with open(po_file_path, "w") as f:
                    f.write(po_content)

                print(f"Created {po_file_path}")

    def _convert_kw_files(self):
        """Convert KW files to Page files"""
        kw_dir = os.path.join(self.robot_dir, "KW")

        for file_name in os.listdir(kw_dir):
            if file_name.endswith(".robot"):
                robot_file_path = os.path.join(kw_dir, file_name)

                # Generate Page file name (e.g., kwSearch.robot -> search.py)
                base_name = file_name[2:-6].lower()  # Remove 'kw' prefix and '.robot' suffix
                page_file_name = f"{base_name}.py"
                page_file_path = os.path.join(self.pages_dir, page_file_name)

                # Skip if file already exists
                if os.path.exists(page_file_path):
                    print(f"Skipping {page_file_name} as it already exists.")
                    continue

                print(f"Converting {file_name} to {page_file_name}")

                # Parse the Robot file to extract keywords
                keywords = self._extract_keywords_from_robot(robot_file_path)

                # Generate the Page class content
                page_content = self._generate_page_class(base_name, keywords)

                # Write the Page file
                with open(page_file_path, "w") as f:
                    f.write(page_content)

                print(f"Created {page_file_path}")

    def _convert_test_files(self):
        """Convert Test files to Playwright test files"""
        test_dirs = [os.path.join(self.robot_dir, "Tests", "Regression"), os.path.join(self.robot_dir, "Tests", "Sanity")]

        for test_dir in test_dirs:
            if not os.path.exists(test_dir):
                continue

            for file_name in os.listdir(test_dir):
                if file_name.endswith(".robot"):
                    robot_file_path = os.path.join(test_dir, file_name)

                    # Generate test file name (e.g., Fin-Portal_Manual_Auth_Sanity.robot -> test_manual_auth.py)
                    base_name = self._clean_test_name(file_name)
                    test_file_name = f"test_{base_name}.py"
                    test_file_path = os.path.join(self.tests_dir, test_file_name)

                    # Skip if file already exists
                    if os.path.exists(test_file_path):
                        print(f"Skipping {test_file_name} as it already exists.")
                        continue

                    print(f"Converting {file_name} to {test_file_name}")

                    # Parse the Robot file to extract test cases
                    test_cases = self._extract_test_cases_from_robot(robot_file_path)

                    # Generate the test class content
                    test_content = self._generate_test_class(base_name, test_cases)

                    # Write the test file
                    with open(test_file_path, "w") as f:
                        f.write(test_content)

                    print(f"Created {test_file_path}")

    def _update_page_initializer(self):
        """Update page_initializer.py with new pages"""
        page_initializer_path = os.path.join(self.base_dir, "base", "page_initializer.py")

        # Get existing content
        with open(page_initializer_path, "r") as f:
            content = f.read()

        # Get all page files
        page_files = [f[:-3] for f in os.listdir(self.pages_dir) if f.endswith(".py") and not f.startswith("__")]

        # Generate imports
        imports = []
        for page_file in page_files:
            class_name = self._to_camel_case(page_file) + "Page"
            import_line = f"from pages.{page_file} import {class_name}"
            if import_line not in content:
                imports.append(import_line)

        # Generate initializations
        inits = []
        for page_file in page_files:
            class_name = self._to_camel_case(page_file) + "Page"
            attr_name = f"self.{page_file}_page"
            init_line = f"        {attr_name} = {class_name}(page)"
            if attr_name not in content:
                inits.append(init_line)

        if not imports and not inits:
            print("No updates needed for page_initializer.py")
            return

        # Update content
        if imports:
            # Find the last import and add new imports after it
            import_section_end = content.rfind("import") + content[content.rfind("import") :].find("\n") + 1
            content = content[:import_section_end] + "\n" + "\n".join(imports) + content[import_section_end:]

        if inits:
            # Find the initialize_pages method and add new initializations before the end
            init_method_end = content.rfind("    def initialize_pages")
            init_method_body_end = content.find("\n\n", init_method_end)
            if init_method_body_end == -1:
                init_method_body_end = len(content)

            content = content[:init_method_body_end] + "\n" + "\n".join(inits) + content[init_method_body_end:]

        # Write updated content
        with open(page_initializer_path, "w") as f:
            f.write(content)

        print(f"Updated {page_initializer_path}")

    def _extract_variables_from_robot(self, robot_file_path):
        """Extract variables from a Robot Framework file"""
        variables = {}
        variable_section = False

        with open(robot_file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.strip()

                if "*** Variables ***" in line:
                    variable_section = True
                    continue

                if line.startswith("***") and variable_section:
                    variable_section = False
                    continue

                if variable_section and line and not line.startswith("#"):
                    parts = line.split("    ", 1)
                    if len(parts) == 2:
                        var_name = parts[0].strip()
                        var_value = parts[1].strip()

                        # Remove ${} from variable name
                        var_name = var_name.replace("${", "").replace("}", "")

                        # Clean up the selector value
                        var_value = var_value.replace("xpath=", "").replace("css=", "")

                        variables[var_name] = var_value

        return variables

    def _extract_keywords_from_robot(self, robot_file_path):
        """Extract keywords from a Robot Framework file"""
        keywords = {}
        current_keyword = None
        keyword_section = False
        keyword_lines = []

        with open(robot_file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.rstrip()

                if "*** Keywords ***" in line:
                    keyword_section = True
                    continue

                if line.startswith("***") and keyword_section:
                    keyword_section = False

                    # Save the last keyword if any
                    if current_keyword:
                        keywords[current_keyword] = keyword_lines
                        current_keyword = None
                        keyword_lines = []

                    continue

                if not keyword_section:
                    continue

                if line and not line.startswith(" ") and not line.startswith("\t") and not line.startswith("#"):
                    # Save the previous keyword if any
                    if current_keyword:
                        keywords[current_keyword] = keyword_lines
                        keyword_lines = []

                    current_keyword = line.strip()
                elif current_keyword and line.strip():
                    keyword_lines.append(line.strip())

        # Save the last keyword if any
        if current_keyword and keyword_lines:
            keywords[current_keyword] = keyword_lines

        return keywords

    def _extract_test_cases_from_robot(self, robot_file_path):
        """Extract test cases from a Robot Framework file"""
        test_cases = {}
        current_test = None
        test_section = False
        test_lines = []
        documentation = ""
        tags = []

        with open(robot_file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.rstrip()

                if "*** Test Cases ***" in line:
                    test_section = True
                    continue

                if line.startswith("***") and test_section:
                    test_section = False

                    # Save the last test if any
                    if current_test:
                        test_cases[current_test] = {"lines": test_lines, "documentation": documentation, "tags": tags}
                        current_test = None
                        test_lines = []
                        documentation = ""
                        tags = []

                    continue

                if not test_section:
                    continue

                if line and not line.startswith(" ") and not line.startswith("\t") and not line.startswith("#"):
                    # Save the previous test if any
                    if current_test:
                        test_cases[current_test] = {"lines": test_lines, "documentation": documentation, "tags": tags}
                        test_lines = []
                        documentation = ""
                        tags = []

                    current_test = line.strip()
                elif current_test and line.strip():
                    stripped_line = line.strip()
                    test_lines.append(stripped_line)

                    # Extract documentation and tags
                    if "[Documentation]" in stripped_line:
                        documentation = stripped_line.replace("[Documentation]", "").strip()
                    elif "[Tags]" in stripped_line:
                        tag_line = stripped_line.replace("[Tags]", "").strip()
                        tags = [tag.strip() for tag in tag_line.split()]

        # Save the last test if any
        if current_test and test_lines:
            test_cases[current_test] = {"lines": test_lines, "documentation": documentation, "tags": tags}

        return test_cases

    def _generate_po_class(self, base_name, variables):
        """Generate a Page Object class from Robot Framework variables"""
        class_name = self._to_camel_case(base_name) + "PO"

        # Define constants for selectors
        constants = []
        for var_name, var_value in variables.items():
            constant_name = self._to_constant_name(var_name)
            if var_value.startswith('"') and var_value.endswith('"'):
                var_value = var_value[1:-1]
            constants.append(f'{constant_name} = "{var_value}"')

        # Define class attributes
        attributes = []
        for var_name, _ in variables.items():
            constant_name = self._to_constant_name(var_name)
            attr_name = self._to_snake_case(var_name)
            attributes.append(f'        self.{attr_name} = self.locator({constant_name}, "{self._generate_description(var_name)}")')

        template = f"""from base.page_base import PageBase

# {base_name.capitalize()} locators converted from or{self._to_camel_case(base_name)}.robot
{os.linesep.join(constants)}

class {class_name}(PageBase):
    \"\"\"Page object for {base_name.capitalize()} functionality\"\"\"
    
    def __init__(self, page):
        super().__init__(page)
{os.linesep.join(attributes)}
"""
        return template

    def _generate_page_class(self, base_name, keywords):
        """Generate a Page class from Robot Framework keywords"""
        po_class_name = self._to_camel_case(base_name) + "PO"
        class_name = self._to_camel_case(base_name) + "Page"

        # Convert keywords to methods
        methods = []
        for keyword, lines in keywords.items():
            # Skip Setup/Teardown
            if keyword.lower() in ["setup", "teardown"]:
                continue

            method_name = self._to_snake_case(keyword)
            method_params = []
            method_body = []

            # Check if the keyword has arguments
            if "[Arguments]" in [line.split("    ")[0] for line in lines if "    " in line]:
                # Extract arguments
                for line in lines:
                    if line.startswith("[Arguments]"):
                        args = line.replace("[Arguments]", "").strip().split("    ")
                        for arg in args:
                            if arg.strip():
                                arg_name = arg.replace("${", "").replace("}", "")
                                method_params.append(arg_name)
                        break

            # Process the lines to generate method body
            for line in lines:
                if line.startswith("[Arguments]") or not line.strip():
                    continue

                action, *args = line.split("    ")
                action = action.strip()

                if action == "Click Element":
                    if len(args) >= 1:
                        element = args[0].strip()
                        element_name = element.replace("${", "").replace("}", "")
                        method_body.append(f"        self.click(self.{self._to_snake_case(element_name)})")
                elif action == "Input Text":
                    if len(args) >= 2:
                        element = args[0].strip()
                        text = args[1].strip()
                        element_name = element.replace("${", "").replace("}", "")
                        if text.startswith("${") and text.endswith("}"):
                            text_var = text.replace("${", "").replace("}", "")
                            method_body.append(f"        self.fill(self.{self._to_snake_case(element_name)}, {text_var})")
                        else:
                            method_body.append(f'        self.fill(self.{self._to_snake_case(element_name)}, "{text}")')
                elif action == "Wait Until Page Contains":
                    if len(args) >= 1:
                        text = args[0].strip()
                        if text.startswith("${") and text.endswith("}"):
                            text_var = text.replace("${", "").replace("}", "")
                            method_body.append(f"        self.wait_for_text({text_var})")
                        else:
                            method_body.append(f'        self.wait_for_text("{text}")')
                else:
                    # For other actions, add a comment
                    method_body.append(f"        # {line}")

            # If method body is empty, add a pass statement
            if not method_body:
                method_body = ["        pass"]

            # Create method
            methods.append(
                f"""    def {method_name}({', '.join(['self'] + method_params)}):
        \"\"\"Converted from Robot Framework keyword: {keyword}\"\"\"
{os.linesep.join(method_body)}
"""
            )

        template = f"""from pos.{base_name}_po import {po_class_name}


class {class_name}({po_class_name}):
    \"\"\"Page class for {base_name.capitalize()} functionality\"\"\"
    
{os.linesep.join(methods)}"""
        return template

    def _generate_test_class(self, base_name, test_cases):
        """Generate a test class from Robot Framework test cases"""
        class_name = f"Test{self._to_camel_case(base_name)}"

        # Convert test cases to test methods
        methods = []
        for test_name, test_data in test_cases.items():
            lines = test_data["lines"]
            documentation = test_data["documentation"]
            tags = test_data["tags"]

            method_name = self._to_snake_case(test_name.replace(" | ", "_").replace("|", "_"))
            method_name = f"test_{method_name}"

            # Add pytest markers from tags
            markers = []
            for tag in tags:
                markers.append(f"@pytest.mark.{tag.lower().replace('-', '_')}")

            # Create method body with steps
            method_body = []
            current_step = ""

            for line in lines:
                # Skip setup/teardown
                if line.startswith("[Setup]") or line.startswith("[Teardown]"):
                    continue

                if line.startswith("["):
                    continue

                parts = line.split("    ")
                if len(parts) >= 2:
                    action = parts[0].strip()
                    args = [p.strip() for p in parts[1:] if p.strip()]

                    # Use action as step description
                    if action and action != current_step:
                        current_step = action
                        method_body.append(f"")  # Add blank line before step
                        method_body.append(f'        self.step("{action}")')

                    # Convert action to page method call
                    if args:
                        arg_str = ", ".join([f'"{arg}"' if not arg.startswith("${") else arg.replace("${", "").replace("}", "") for arg in args])
                        method_body.append(f"        self.{self._map_page_method(action)}({arg_str})")
                    else:
                        method_body.append(f"        self.{self._map_page_method(action)}()")

            # If method body is empty, add a pass statement
            if not method_body:
                method_body = ["        pass"]

            # Create method
            methods.append(
                f"""{'    ' + os.linesep.join(markers) if markers else ''}
    def {method_name}(self):
        \"\"\"{'No documentation' if not documentation else documentation}\"\"\"
{os.linesep.join(method_body)}
"""
            )

        template = f"""import pytest
from base.test_base import TestBase


class {class_name}(TestBase):
    \"\"\"Tests for {base_name.replace('_', ' ').title()} functionality\"\"\"
    
{os.linesep.join(methods)}"""
        return template

    def _map_page_method(self, action):
        """Map robot action to page method call"""
        # This is a simple mapping function - expand as needed
        action_lower = action.lower()

        if "login" in action_lower:
            return "login_page.login"
        elif "search" in action_lower and "customer" in action_lower:
            return "search_page.search_for_customer"
        elif "search" in action_lower and "order" in action_lower:
            return "search_page.search_for_order"
        elif "click" in action_lower and "payment" in action_lower:
            return "order_view_page.click_payments_ledger_accordion"
        else:
            # Default fallback
            page_name = action_lower.split(" ")[0] + "_page"
            method_name = self._to_snake_case(action)
            return f"{page_name}.{method_name}"

    def _clean_test_name(self, file_name):
        """Clean test file name for Python naming conventions"""
        # Remove Fin-Portal_ prefix and _Sanity/_Regression suffix
        name = file_name.replace(".robot", "")
        name = re.sub(r"^Fin-Portal_", "", name)
        name = re.sub(r"_(Sanity|Regression)$", "", name)

        # Convert to snake_case
        name = self._to_snake_case(name)

        return name

    def _to_camel_case(self, name):
        """Convert string to CamelCase"""
        # Split by non-alphanumeric characters
        parts = re.split(r"[^a-zA-Z0-9]", name)
        # Capitalize first letter of each part and join
        return "".join(part.capitalize() for part in parts if part)

    def _to_snake_case(self, name):
        """Convert string to snake_case"""
        # Replace non-alphanumeric with underscore
        name = re.sub(r"[^a-zA-Z0-9]", "_", name)
        # Insert underscore before uppercase letters
        name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
        # Convert to lowercase
        return name.lower()

    def _to_constant_name(self, name):
        """Convert string to CONSTANT_NAME"""
        return self._to_snake_case(name).upper()

    def _generate_description(self, name):
        """Generate a human-readable description from a variable name"""
        # Remove 'btn', 'txt', 'ddl' prefixes
        cleaned_name = re.sub(r"^(btn|txt|ddl)", "", name)
        # Split by capital letters
        parts = re.findall(r"[A-Z][a-z0-9]*", cleaned_name)
        # Join with spaces and capitalize first letter
        if parts:
            return " ".join(parts).capitalize()
        else:
            return cleaned_name.capitalize()


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    converter = RobotToPlaywrightConverter(base_dir)
    result = converter.convert_all()
    print(result)
