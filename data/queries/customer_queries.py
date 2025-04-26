"""
Contains SQL queries related to customers
"""


class CustomerQueries:
    """SQL queries for customers and their related operations"""

    # Basic customer queries
    customer_with_valid_credit = """
        select idCustomer, FirstName, LastName, Credit
        from take2.customers
        where Credit > 100 and Active = 1
        order by Credit desc
        limit 1
    """

    customer_with_valid_email_sql = """
        select idCustomer, Email, FirstName, LastName
        from take2.customers
        where Email LIKE '%@%' and Email NOT LIKE '%takealot%'
        and Active = 1
        order by idCustomer desc
        limit 1
    """

    registered_customer_sql = """
        select idCustomer, Email, FirstName, LastName, DateCreated
        from take2.customers
        where Active = 1
        order by idCustomer desc
        limit 1
    """

    anonymous_customer_sql = """
        select idCustomer, Email, FirstName, LastName
        from take2.customers
        where Active = 1 and Anonymous = 1
        order by idCustomer desc
        limit 1
    """

    inactive_customer_sql = """
        select idCustomer, Email, FirstName, LastName, Active
        from take2.customers
        where Active = 0
        order by idCustomer desc
        limit 1
    """

    # Customer type or attribute specific queries
    staff_customer_sql = """
        select idCustomer, Email, FirstName, LastName, StaffMember
        from take2.customers
        where StaffMember = 1 and Active = 1
        order by idCustomer desc
        limit 1
    """

    customer_with_customer_type_sql = """
        select idCustomer, (select id from CustomerType where id = c.CustomerType) as CustomerType
        from take2.customers c
        where c.CustomerType = 7
        order by idCustomer desc
        limit 1
    """

    customer_with_sub_type_sql = """
        select idCustomer, SubType.name
        from take2.customers c
        left join CustomerSubType as SubType on SubType.id = c.CustomerSubType
        where c.CustomerSubType = 4
        order by idCustomer desc
        limit 1
    """

    recurring_customer_sql = """
        select c.idCustomer, c.Email, c.FirstName, c.LastName, count(distinct o.idOrder) as OrderCount
        from take2.customers c
        join take2.orders o on c.idCustomer = o.idCustomer
        where c.Active = 1
        group by c.idCustomer
        having OrderCount > 5
        order by OrderCount desc
        limit 1
    """

    # Credit related queries
    customer_with_highest_credit_sql = """
        select idCustomer, Email, FirstName, LastName, Credit
        from take2.customers
        where Credit > 0 and Active = 1
        order by Credit desc
        limit 1
    """

    customer_with_negative_credit_sql = """
        select idCustomer, Email, FirstName, LastName, Credit
        from take2.customers
        where Credit < 0 and Active = 1
        order by Credit asc
        limit 1
    """

    customer_with_zero_credit_sql = """
        select idCustomer, Email, FirstName, LastName, Credit
        from take2.customers
        where Credit = 0 and Active = 1
        order by idCustomer desc
        limit 1
    """

    # Address related queries
    customer_with_address_sql = """
        select c.idCustomer, c.Email, c.FirstName, c.LastName, a.AddressName
        from take2.customers c
        join take2.customeraddresses a on c.idCustomer = a.idCustomer
        where c.Active = 1
        order by c.idCustomer desc
        limit 1
    """

    customer_with_multiple_addresses_sql = """
        select c.idCustomer, c.Email, c.FirstName, c.LastName, count(a.idAddress) as AddressCount
        from take2.customers c
        join take2.customeraddresses a on c.idCustomer = a.idCustomer
        where c.Active = 1
        group by c.idCustomer
        having AddressCount > 1
        order by AddressCount desc
        limit 1
    """

    # Voucher related queries
    customer_with_unused_voucher_sql = """
        select c.idCustomer, c.Email, c.FirstName, c.LastName, v.Code, v.Value
        from take2.customers c
        join take2.vouchers v on c.idCustomer = v.idCustomer
        where v.Used = 0 and v.Expired = 0
        and c.Active = 1
        order by c.idCustomer desc
        limit 1
    """

    customer_with_expired_voucher_sql = """
        select c.idCustomer, c.Email, c.FirstName, c.LastName, v.Code, v.Value
        from take2.customers c
        join take2.vouchers v on c.idCustomer = v.idCustomer
        where v.Expired = 1
        and c.Active = 1
        order by v.DateExpired desc
        limit 1
    """

    customer_with_used_voucher_sql = """
        select c.idCustomer, c.Email, c.FirstName, c.LastName, v.Code, v.Value
        from take2.customers c
        join take2.vouchers v on c.idCustomer = v.idCustomer
        where v.Used = 1
        and c.Active = 1
        order by v.DateUsed desc
        limit 1
    """

    customer_with_highest_voucher_value_sql = """
        select c.idCustomer, c.Email, c.FirstName, c.LastName, v.Code, v.Value
        from take2.customers c
        join take2.vouchers v on c.idCustomer = v.idCustomer
        where v.Used = 0 and v.Expired = 0
        and c.Active = 1
        order by v.Value desc
        limit 1
    """
