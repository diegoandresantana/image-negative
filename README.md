# 🖼️ pyNegative - Processador de Imagens com OpenCV

Uma aplicação GUI em Python para processamento de imagens usando OpenCV, que permite visualizar diferentes técnicas de transformação e thresholding em tempo real.

<div align="center">
  <img src="https://img.shields.io/badge/Python-2.7-blue.svg" alt="Python Version"/>
  <img src="https://img.shields.io/badge/OpenCV-Computer_Vision-green.svg" alt="OpenCV"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License"/>
</div>

## 📋 Sobre o Projeto

O **pyNegative** é uma aplicação desktop que fornece uma interface gráfica intuitiva para processamento e análise de imagens. A ferramenta aplica diversas transformações morfológicas e técnicas de thresholding, exibindo os resultados lado a lado para comparação.

### ✨ Funcionalidades

- 📁 **Seleção de Imagens**: Interface para carregar imagens nos formatos JPG e PNG
- 🔄 **Transformações em Tempo Real**:
  - Conversão para escala de cinza (GRAY)
  - Thresholding binário (BINARY)
  - Detecção de contornos (CONTOURS)
  - Thresholding adaptativo Gaussiano (ADAPTIVE_THRESH_GAUSSIAN_C)
  - Thresholding binário invertido (BINARY_INV)
  - Thresholding truncado (TRUNC)
  - Thresholding TOZERO
  - Thresholding TOZERO invertido (TOZERO_INV)
- 🖼️ **Visualização Multipla**: Exibe até 9 variações da imagem simultaneamente
- 🎯 **Interface Amigável**: Layout organizado com controles intuitivos

## 🚀 Instalação

### Pré-requisitos

Certifique-se de ter instalado:

1. **Python 2.7** ou superior
   ```bash
   # Verificar versão do Python
   python --version
   ```

2. **OpenCV** (opencv-python)
   ```bash
   pip install opencv-python
   ```

3. **Pillow** (PIL)
   ```bash
   pip install Pillow
   ```

4. **NumPy**
   ```bash
   pip install numpy
   ```

5. **Tkinter** (geralmente incluído com Python)
   ```bash
   # Ubuntu/Debian
   sudo apt-get install python-tk
   
   # Windows/Mac: Já vem com a instalação padrão do Python
   ```

### Instalação Rápida

```bash
# Clone este repositório
git clone <URL_DO_REPOSITORIO>

# Navegue até o diretório
cd pyNegative

# Instale as dependências
pip install -r requirements.txt
```

## 💻 Como Usar

1. Execute o script principal:
   ```bash
   python pyNegative.py
   ```

2. Na interface que abrir:
   - Clique em **"Selecione a Imagem"** para carregar uma imagem (JPG ou PNG)
   - Clique em **"Executar Procedimentos"** para aplicar todas as transformações
   - Visualize os resultados em tempo real nos painéis à direita

## 📁 Estrutura do Projeto

```
pyNegative/
├── pyNegative.py          # Script principal da aplicação
├── README.md              # Documentação do projeto
├── requirements.txt       # Dependências do projeto
├── docs/                  # Documentação para GitHub Pages
│   └── index.html         # Página estática do projeto
└── .gitignore             # Arquivos ignorados pelo Git
```

## 🔧 Tecnologias Utilizadas

- **Python 2.7+** - Linguagem de programação principal
- **OpenCV** - Processamento de imagens e visão computacional
- **Tkinter** - Interface gráfica do usuário (GUI)
- **Pillow (PIL)** - Manipulação e exibição de imagens
- **NumPy** - Operações numéricas com arrays

## 📸 Screenshots

<div align="center">
  <p>A aplicação exibe múltiplas visualizações da mesma imagem com diferentes transformações aplicadas.</p>
</div>

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

**Diego André Sant'Ana**  
Email: [diego.santana@ifms.edu.br](mailto:diego.santana@ifms.edu.br)

## 🙏 Agradecimentos

- OpenCV pela excelente biblioteca de visão computacional
- Comunidade Python pelo suporte e ferramentas incríveis

---

<div align="center">
  <p>Feito com ❤️ usando Python e OpenCV</p>
  <p>⭐ Se este projeto foi útil, considere dar uma estrela!</p>
</div>  


