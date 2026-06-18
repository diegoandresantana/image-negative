# 🖼️ pyNegative - Processador de Imagens com OpenCV

Uma aplicação GUI em Python para processamento de imagens usando OpenCV, que permite visualizar diferentes técnicas de transformação e thresholding em tempo real.

<div align="center">
  <img src="https://img.shields.io/badge/Python-2.7-blue.svg" alt="Python Version"/>
  <img src="https://img.shields.io/badge/OpenCV-Computer_Vision-green.svg" alt="OpenCV"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License"/>
</div>

## 📋 Sobre o Projeto

O **pyNegative** é uma aplicação para processamento e análise de imagens disponível em duas versões:

1. **Versão Desktop (Python)**: Interface gráfica usando Tkinter para processamento de imagens
2. **Versão Web (HTML/JS)**: Aplicação interativa que roda diretamente no navegador, sem necessidade de instalação

Ambas as versões aplicam diversas transformações morfológicas e técnicas de thresholding, exibindo os resultados lado a lado para comparação.

### ✨ Funcionalidades

- 📁 **Seleção de Imagens**: Interface para carregar imagens nos formatos JPG e PNG
- 🔄 **Transformações Disponíveis**:
  - Conversão para escala de cinza (GRAY)
  - Thresholding binário (BINARY) - limiar em 127
  - Detecção de contornos (CONTOURS)
  - Thresholding adaptativo Gaussiano (ADAPTIVE_THRESH_GAUSSIAN_C)
  - Thresholding binário invertido (BINARY_INV)
  - Thresholding truncado (TRUNC)
  - Thresholding TOZERO
  - Thresholding TOZERO invertido (TOZERO_INV)
- 🖼️ **Visualização Múltipla**: Exibe até 9 variações da imagem simultaneamente
- 🌐 **Versão Web**: Teste diretamente no navegador sem instalar nada! Acesse em: [https://SEU-USUARIO.github.io/pyNegative](https://SEU-USUARIO.github.io/pyNegative)

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
├── pyNegative.py          # Script principal (Python/Tkinter)
├── README.md              # Documentação do projeto
├── docs/                  # Aplicação Web para GitHub Pages
│   └── index.html         # Versão web interativa (HTML5/JS)
└── .gitignore             # Arquivos ignorados pelo Git
```

## 🔧 Tecnologias Utilizadas

### Versão Desktop (Python)
- **Python 2.7+** - Linguagem de programação principal
- **OpenCV** - Processamento de imagens e visão computacional
- **Tkinter** - Interface gráfica do usuário (GUI)
- **Pillow (PIL)** - Manipulação e exibição de imagens
- **NumPy** - Operações numéricas com arrays

### Versão Web (GitHub Pages)
- **HTML5 Canvas** - Renderização de imagens no navegador
- **JavaScript** - Processamento de imagens no cliente
- **CSS3** - Estilização e layout responsivo

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

## 🌐 GitHub Pages

Este projeto possui uma versão web interativa disponível no **GitHub Pages**! 

### Como Ativar o GitHub Pages:

1. Vá até as **Settings** do seu repositório no GitHub
2. Clique em **Pages** na barra lateral esquerda
3. Em **Source**, selecione a branch `main` (ou `master`)
4. Em **Folder**, selecione `/docs`
5. Clique em **Save**

Após alguns minutos, sua aplicação estará disponível em:
```
https://SEU-USUARIO.github.io/pyNegative/
```

### Vantagens da Versão Web:
- ✅ Não requer instalação de Python ou dependências
- ✅ Funciona em qualquer navegador moderno
- ✅ Processamento local no navegador (sem envio de dados)
- ✅ Interface responsiva para desktop e mobile
- ✅ Mesmas transformações da versão desktop

---

<div align="center">

  <p>Feito usando Python e OpenCV</p>

  <p>⭐ Se este projeto foi útil, considere dar uma estrela!</p>
</div>  


