def test_validar_conteudo_do_arquivo_gerado():
    analyze_log("data/orders_1.csv")
    FILE_TXT = "data/mkt_campaign.txt"
    with open(FILE_TXT) as f:
        file_txt_file = f.readlines()
        (
            maria_eats,
            arnaldo_ask_hamburguer,
            joao_never_ask,
            joao_never_went,
        ) = file_txt_file
    assert maria_eats == "hamburguer\n"
    assert arnaldo_ask_hamburguer == "1\n"
    assert eval(joao_never_ask) == {"pizza", "coxinha", "misto-quente"}
    assert eval(joao_never_went) == {"sabado", "segunda-feira"}

