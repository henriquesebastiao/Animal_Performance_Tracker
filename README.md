# Animal Performance Tracker

Este é um programa em Python para gerenciamento e monitoramento de desempenho de criações de animais.

#### O programa permite aos usuários registrar informações detalhadas sobre seus animais, incluindo:
- ID
- Raça
- Idade
- Peso
- Porte
- Data de entrada
- Origem

Com esses dados, é possível monitorar o desempenho dos animais ao longo do tempo e analisar tendências e padrões.

### Recursos futuros:
Análise de dados incluindo gráficos e relatórios personalizados, para ajudar os usuários a entender melhor o desempenho de seus animais.

### Instalação:
<details open><summary><strong>Ubuntu</strong></summary>

#### Ubuntu:
```bash
sudo apt install python3.10 python3-pip
pip3 install virtualenv
git clone https://github.com/henriquesebastiao/Animal_Performance_Tracker.git
cd Animal_Performance_Tracker
virtualenv -p python3.10 venv
source venv/bin/activate
pip install -r requirements.txt
```
</details>
<details><summary><strong>Fedora</strong></summary>

```bash
sudo dnf install python3.10 python3-pip
pip3 install virtualenv
git clone https://github.com/henriquesebastiao/Animal_Performance_Tracker.git
cd Animal_Performance_Tracker
virtualenv -p python3.10 venv
source venv/bin/activate
pip install -r requirements.txt
```
</details>
<details><summary><strong>Arch</strong></summary>

```bash
sudo pacman -S python3.10 python3-pip
pip3 install virtualenv
git clone https://github.com/henriquesebastiao/Animal_Performance_Tracker.git
cd Animal_Performance_Tracker
virtualenv -p python3.10 venv
source venv/bin/activate
pip install -r requirements.txt
```
</details>

### Como usar:
1. Dentro do diretório do projeto, execute o seguinte comando:
```bash
python3 main.py
```
2. Siga as instruções na tela.