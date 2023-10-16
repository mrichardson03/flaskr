def test_initialize_database(cli_test_client):
    output = cli_test_client.invoke(args=["init-db"])
    assert output.exit_code == 0
    assert "Initialized the database." in output.output
