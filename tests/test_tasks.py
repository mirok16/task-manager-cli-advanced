def test_add():
    add_task("A")
    assert len(list_tasks()) > 0
