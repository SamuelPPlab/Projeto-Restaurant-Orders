import csv

def analyze_log(path_to_file):
    with open(path_to_file) as file:
        file = csv.reader(file, delimiter=",", quotechar='"')
        maria = {}
        maria_favorite = ""
        arnaldo_hamburguer_count = 0
        joao_asked = set()
        joao_not_asked = set()
        joao_came = set()
        joao_didt_come = set()

        for line in file:
          # joao
          if line[0] == 'joao': joao_asked.add(line[1])
          else: joao_not_asked.add(line[1])
          # joao came
          if line[0] == 'joao': joao_came.add(line[2])
          else: joao_didt_come.add(line[2])
          # maria
          if (line[0] == "maria"):
            if (line[1] in maria.keys()):
              maria[line[1]] += 1
            else:
              maria[line[1]] = 1
          # arnaldo_hamburger_count
          if (line[0] == "arnaldo" and line[1] == "hamburguer"): arnaldo_hamburguer_count += 1
        
        # get maria_favorite
        for key in maria.keys():
          if (maria_favorite == ""):
            maria_favorite = key
          if (maria[key] > maria[maria_favorite]):
            maria_favorite = key

        stringao = f"""{str(maria_favorite)}
{str(arnaldo_hamburguer_count)}
{str(joao_not_asked-joao_asked)}
{str(joao_didt_come-joao_came)}"""
        print(stringao)
        f = open("data/mkt_campaign.txt", "w")
        f.write(stringao)
        f.close()

if __name__ == '__main__':
    analyze_log("data/orders_1.csv")