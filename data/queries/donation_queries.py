"""
Contains SQL queries related to donations
"""


class DonationQueries:
    """SQL queries for donations and their related operations"""

    donation_sql = """
        select o.idOrder, d.Amount, d.Name
        from take2.orders o
        join take2.donations d on o.idOrder = d.idOrder
        order by o.OrderDate desc
        limit 1
    """

    donation_with_specific_charity_sql = """
        select o.idOrder, d.Amount, d.Name
        from take2.orders o
        join take2.donations d on o.idOrder = d.idOrder
        where d.Name = 'Afrika Tikkun'
        order by o.OrderDate desc
        limit 1
    """

    donation_with_amount_above_threshold_sql = """
        select o.idOrder, d.Amount, d.Name
        from take2.orders o
        join take2.donations d on o.idOrder = d.idOrder
        where d.Amount > 50
        order by d.Amount desc
        limit 1
    """
