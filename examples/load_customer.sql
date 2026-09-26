DECLARE
  v_name VARCHAR2(100);
BEGIN
  SELECT customer_name INTO v_name
  FROM customers
  WHERE customer_id = 42;
EXCEPTION
  WHEN NO_DATA_FOUND THEN
    log_error('Customer not found');
    RAISE;
  WHEN DUP_VAL_ON_INDEX THEN
    log_error('Duplicate');
  WHEN OTHERS THEN
    log_error(SQLERRM);
    RAISE;
END;
/
