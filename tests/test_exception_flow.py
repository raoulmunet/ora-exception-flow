from ora_exception_flow import parse_handlers,render_mermaid

PLSQL="""BEGIN
  SELECT 1 INTO v_x FROM dual;
EXCEPTION
  WHEN NO_DATA_FOUND THEN
    log_error('missing');
    RAISE;
  WHEN OTHERS THEN
    log_error('other');
END;"""

def test_handlers():
    h=parse_handlers(PLSQL)
    assert h[0].exceptions==["NO_DATA_FOUND"]
    assert h[0].reraises is True
    assert h[1].reraises is False
    assert "NO_DATA_FOUND" in render_mermaid(h)
