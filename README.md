# Biografia Linguística — Mario Morales

**Abrir a apresentação:** https://yeridu.github.io/biografia-linguistica-por305/

Apresentação final para o curso POR 305 (Universidade do Arizona). Página web de slides em português, com foto, vídeo, navegação por teclado e notas do apresentador.

## Como abrir

### Opção 1 — Localmente (mais simples)
Abra `index.html` com um duplo clique. A página carrega direto no navegador.

### Opção 2 — Servidor local (recomendado para ver o vídeo em qualquer navegador)
Na pasta `BiografiaMarioMorales`:

```bash
python -m http.server 8000
```

Depois abra `http://localhost:8000/` no navegador.

### Opção 3 — GitHub Pages
1. Faça push da pasta `BiografiaMarioMorales` para um repositório no GitHub.
2. Em *Settings → Pages*, selecione o branch e a raiz do repositório.
3. A página ficará disponível em `https://<seu-usuario>.github.io/<nome-do-repositorio>/`.

Os caminhos para `assets/` são relativos, então a página funciona tanto localmente quanto no GitHub Pages.

## Atalhos de teclado

| Tecla | Ação |
|-------|------|
| `←` / `PageUp` | Slide anterior |
| `→` / `PageDown` / `Espaço` | Próximo slide |
| `S` | Mostrar / esconder notas do apresentador |
| `F` | Alternar tela cheia |
| `Home` | Primeiro slide |
| `End` | Último slide |
| `Esc` | Fechar notas do apresentador |

Também é possível:
- Clicar nos botões **Anterior** e **Próximo** no rodapé.
- Deslizar o dedo para a esquerda ou direita no celular.
- Acessar um slide direto pela URL: `index.html#3` abre o slide 3.

## Estrutura dos slides

1. Abertura — título, foto, ideia principal.
2. Três línguas, três portas — mapa das três línguas + linha do tempo (México, Tucson, Belize, sala de português).
3. México — espanhol como língua da memória.
4. Tucson — inglês como língua do trabalho e do doutorado.
5. Belize — colaboração, escuta, pesquisa, cuidado.
6. Português — uma nova porta para o Brasil.
7. Pantanal e One Health — onças-pintadas e a ideia de Saúde Única.
8. Automedicando a Dor Social — vídeo com legenda.
9. Fecho — três línguas, uma vida.

Cada slide tem **notas do apresentador** curtas em português. Tecle `S` para ver as notas durante a apresentação.

## Gerar PDF de backup

A página tem CSS dedicado para impressão (`@media print`). Para gerar um PDF:

1. Abra `index.html` no navegador.
2. Pressione `Ctrl+P` (Windows) ou `Cmd+P` (Mac).
3. Em *Destino*, escolha "Salvar como PDF".
4. As notas do apresentador aparecem abaixo de cada slide no PDF.

## Conteúdo dos arquivos da pasta

```
BiografiaMarioMorales/
├── index.html                       # Página de slides (HTML + CSS + JS embutidos)
├── README.md                        # Este arquivo
└── assets/
    ├── FestaJunina.jpeg            # Foto da Festa Junina (slide 1)
    ├── Family.jpeg                 # Família no México (slide 3)
    ├── Work.jpeg                   # Trabalho em Tucson (slide 4)
    ├── Belize.jpg                  # Belize (slide 5)
    ├── Brazil.svg                  # Contorno do Brasil (slide 6) - Mapsicon, MIT / baseado em Felipe Menegaz
    ├── Jaguar.jpg                  # Onça-pintada no Pantanal (slide 7) - Charles J. Sharp, CC BY-SA 4.0
    └── Automedicando_a_Dor_Social.mp4  # Vídeo de pesquisa (slide 8)
```

## Design

- Tipografia: **Space Grotesk** (títulos) + **Inter** (corpo), carregadas pelo Google Fonts.
- Paleta: fundo azul-carvão escuro, texto branco-quente, acentos em teal suave e dourado.
- Animações discretas de entrada (fade + rise) respeitam `prefers-reduced-motion`.
- Layout responsivo para laptop, projetor e celular.
- Sem frameworks, sem build tools, sem dependências externas além do Google Fonts.

## Dicas de apresentação

- Duração prevista: **5 a 10 minutos**.
- Antes de começar, tecle `F` para tela cheia e depois `S` se precisar ver as notas.
- No slide 8, clique em play no vídeo quando quiser mostrá-lo. O vídeo para automaticamente ao trocar de slide.
- A versão curta para memorizar está em `BiografiaLinguistica2.md` (na pasta pai do projeto).

## Contato

Mario Morales — doutorando em saúde pública, Universidade do Arizona.
