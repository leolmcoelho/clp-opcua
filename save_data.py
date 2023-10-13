import os
import pandas as pd
import sys
import codecs


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def clearLines(lines=1):
    for line in range(lines):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")


def createDirectory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)



def export_to_xlsx(df=None, directory='resultado', filename_without_extension='file', columns=None):
    try:
        print("Exporting to XLSX...")
        createDirectory(directory)

        # Verificar se o arquivo XLSX existe
        file_path = f"{directory}/{filename_without_extension}.xlsx"
        if os.path.exists(file_path):
            # Carregar a tabela existente em um DataFrame
            existing_df = pd.read_excel(file_path)

            # Concatenar o DataFrame existente com o novo DataFrame
            df = pd.concat([existing_df, df], ignore_index=True)

        # Exportar o DataFrame concatenado para o arquivo XLSX
        df.to_excel(file_path, index=False, columns=columns)

        clearLines()
        print(f"Export to XLSX completed.")

        return file_path
    except Exception as e:
        clearLines()
        print(f"Failed to export to XLSX: {e}")
        return False


def export2JSON(df=None, directory='resultado', filename_without_extension='file'):
    try:
        print("Exporting to JSON...")
        createDirectory(directory)
        file = df.to_json(orient='records', force_ascii=False, index=False)
        file = codecs.open(f"{directory}/{filename_without_extension}.json", "w",
                           "utf-8").write(file).close()

        clearLines()
        print(f"Export to JSON completed.")

        return file
    except Exception:
        clearLines()
        print(f"Failed to export to JSON!")
        return False
        # raise Exception


def createDF(data):
    return pd.DataFrame([data])
    
    
def export_to_csv(df=None, directory='resultado', filename_without_extension='file', columns=None):
    try:
        print("Exporting to CSV...")
        createDirectory(directory)
        
        file_path = f"{directory}/{filename_without_extension}.csv"
        
        if os.path.exists(file_path):
            # Se o arquivo existir, apenas anexe os novos dados
            df.to_csv(file_path, index=False, header=False, mode='a', sep=',', columns=columns)
        else:
            # Caso contrário, crie um novo arquivo
            df.to_csv(file_path, index=False, header=columns, sep=',')

        clearLines()
        print(f"Export to CSV completed.")
        return True
    except Exception:
        clearLines()
        print(f"Failed to export to CSV!")
        return False
