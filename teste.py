import concurrent.futures
import pandas as pd

# Define a função que será executada em paralelo
def processar_jogo(driver, id_jogo):
    # Realize suas operações com o driver e id_jogo aqui
    # Retorne os resultados como um dicionário ou outra estrutura de dados adequada

# ...

if __name__ == "__main__":
    start_time = time.time()
    drivers = []  # Suponha que você tenha uma lista de drivers aqui
    id_jogos = []  # Suponha que você tenha uma lista de IDs de jogos aqui
    
    futures = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as ex:
        for driver, id_jogo in zip(drivers, id_jogos):
            futures.append(ex.submit(processar_jogo, driver, id_jogo))
            
    for future in concurrent.futures.as_completed(futures):
        try:
            df2 = pd.DataFrame(future.result())
            df = df.append(df2, ignore_index=True)
        except:
            pass

    # Resto do seu código para manipular o DataFrame e salvar os resultados

    print(f'% Futures: --- {time.time() - start_time} seconds --- %')
