graph TD
    call_graph --> validate_service_stop_date
    call_graph --> build_conditions
    call_graph --> convert_deferred_expense_to_expense
    call_graph --> convert_deferred_revenue_to_income
    call_graph --> get_booking_dates
    call_graph --> calculate_monthly_amount
    call_graph --> calculate_amount
    call_graph --> get_already_booked_amount
    call_graph --> book_deferred_income_or_expense
    call_graph --> _book_deferred_revenue_or_expense
    call_graph --> process_deferred_accounting
    call_graph --> make_gl_entries
    call_graph --> send_mail
    call_graph --> book_revenue_via_journal_entry
    call_graph --> get_deferred_booking_accounts