-- Tabela: beneficio
CREATE TABLE beneficio (
    idbeneficio SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT NOT NULL,
    criterios TEXT NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    valor NUMERIC(10, 2) NOT NULL CHECK (valor >= 0)
);

-- Tabela: familia
CREATE TABLE familia (
    idfamilia SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    rua VARCHAR(100),
    numero VARCHAR(10),
    bairro VARCHAR(50),
    cidade VARCHAR(50) NOT NULL,
    telefone VARCHAR(20),
    renda NUMERIC(10, 2) NOT NULL CHECK (renda >= 0),
    numeroMembros INT
);

-- Tabela: tem (relação entre família e benefício)
CREATE TABLE tem (
    idfamilia INT,
    idbeneficio INT,
    dataInicio DATE,
    PRIMARY KEY (idfamilia, idbeneficio),
    FOREIGN KEY (idfamilia) REFERENCES familia(idfamilia) ON DELETE CASCADE,
    FOREIGN KEY (idbeneficio) REFERENCES beneficio(idbeneficio) ON DELETE CASCADE
);

-- Tabela: pessoa
CREATE TABLE pessoa (
    NIS VARCHAR(11) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    dataNascimento DATE NOT NULL,
    genero CHAR(1),
    idfamilia INT,
    anoEscolar VARCHAR(20),
    renda NUMERIC(10,2) NOT NULL CHECK (renda >= 0),
    ocupacao VARCHAR(100),
    FOREIGN KEY (idfamilia) REFERENCES familia(idfamilia) ON DELETE CASCADE
);

-- Tabela: agente
CREATE TABLE agente (
    idagente SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    contato VARCHAR(100) NOT NULL,
    login VARCHAR(50) NOT NULL,
    senha VARCHAR(100) NOT NULL
);

-- Tabela: relatorio
CREATE TABLE relatorio (
    idrelatorio SERIAL PRIMARY KEY
);

-- Tabela: visita
CREATE TABLE visita (
    idagente INT,
    idfamilia INT,
    idrelatorio INT,
    data DATE,
    hora TIME NOT NULL,
    status VARCHAR(50) NOT NULL,
    PRIMARY KEY (idagente, idrelatorio),
    FOREIGN KEY (idfamilia) REFERENCES familia(idfamilia) ON DELETE CASCADE,
    FOREIGN KEY (idagente) REFERENCES agente(idagente) ON DELETE CASCADE,
    FOREIGN KEY (idrelatorio) REFERENCES relatorio(idrelatorio) ON DELETE CASCADE
);

-- Tabela: relatorio_observacoes
CREATE TABLE relatorio_observacoes (
    idrelatorio INT PRIMARY KEY,
    observacoes TEXT NOT NULL,
    FOREIGN KEY (idrelatorio) REFERENCES relatorio(idrelatorio) ON DELETE CASCADE
);

-- Tabela: relatorio_vacinacaoFamilia
CREATE TABLE relatorio_vacinacaoFamilia (
    idrelatorio INT PRIMARY KEY,
    vacinacaoFamilia TEXT NOT NULL,
    FOREIGN KEY (idrelatorio) REFERENCES relatorio(idrelatorio) ON DELETE CASCADE
);

-- Tabela: relatorio_pesoFamilia
CREATE TABLE relatorio_pesoFamilia (
    idrelatorio INT PRIMARY KEY,
    pesoFamilia TEXT NOT NULL,
    FOREIGN KEY (idrelatorio) REFERENCES relatorio(idrelatorio) ON DELETE CASCADE
);



--POPULAR TABELA


INSERT INTO beneficio (nome, descricao, criterios, tipo, valor) VALUES
('Auxílio Alimentação', 'Benefício para compra de alimentos', 'Baixa renda', 'Mensal', 200.00),
('Bolsa Família', 'Programa de transferência de renda', 'Famílias com renda per capita baixa', 'Mensal', 300.00),
('Vale Transporte', 'Ajuda com transporte público', 'Trabalhadores formais', 'Mensal', 150.00),
('Auxílio Moradia', 'Ajuda para pagar aluguel', 'Desabrigados ou em situação de risco', 'Mensal', 400.00),
('Auxílio Educação', 'Ajuda para compra de material escolar', 'Famílias com filhos em idade escolar', 'Anual', 250.00),
('Cesta Básica', 'Entrega mensal de alimentos', 'Famílias vulneráveis', 'Mensal', 180.00),
('Auxílio Natalidade', 'Ajuda para recém-nascidos', 'Famílias com recém-nascidos', 'Único', 500.00),
('Isenção de Taxas', 'Isenção de taxas municipais', 'Famílias carentes', 'Anual', 0.00),
('Programa Luz Social', 'Desconto em conta de luz', 'Baixa renda', 'Mensal', 100.00),
('Tarifa Social de Água', 'Desconto na conta de água', 'Famílias com cadastro único', 'Mensal', 80.00);


INSERT INTO familia (nome, rua, numero, bairro, cidade, telefone, renda, numeroMembros) VALUES
('Silva', 'Rua das Flores', '123', 'Centro', 'Cidade A', '1111-1111', 1200.00, 2),
('Souza', 'Av. Brasil', '456', 'Jardim', 'Cidade B', '2222-2222', 800.00, 2),
('Lima', 'Rua A', '789', 'Vila Nova', 'Cidade A', '3333-3333', 600.00, 1),
('Costa', 'Rua B', '321', 'Centro', 'Cidade C', '4444-4444', 1000.00, 1),
('Rocha', 'Rua C', '654', 'Bela Vista', 'Cidade D', '5555-5555', 950.00, 1),
('Melo', 'Rua D', '987', 'Liberdade', 'Cidade A', '6666-6666', 1500.00, 1),
('Dias', 'Rua E', '135', 'Industrial', 'Cidade E', '7777-7777', 700.00, 1),
('Alves', 'Rua F', '246', 'Zona Norte', 'Cidade B', '8888-8888', 400.00, 1),
('Martins', 'Rua G', '357', 'Zona Sul', 'Cidade C', '9999-9999', 1100.00, 0),
('Oliveira', 'Rua H', '468', 'Centro', 'Cidade A', '1010-1010', 500.00, 0);


INSERT INTO tem (idfamilia, idbeneficio, dataInicio) VALUES
(1, 1, '2024-01-01'),
(1, 2, '2024-01-01'),
(2, 2, '2024-02-15'),
(3, 3, '2024-03-10'),
(4, 4, '2024-03-11'),
(5, 5, '2024-01-20'),
(6, 6, '2024-05-25'),
(7, 7, '2024-06-01'),
(8, 8, '2024-06-15'),
(9, 9, '2024-07-01'),
(10, 10, '2024-07-10');


INSERT INTO pessoa (NIS, nome, idade, dataNascimento, genero, idfamilia, anoEscolar, renda, ocupacao) VALUES
('10000000001', 'Ana Silva', 35, '1989-01-01', 'F', 1, 'Ensino Médio', 0.00, 'Doméstica'),
('10000000002', 'Carlos Silva', 40, '1984-03-15', 'M', 1, 'Ensino Fundamental', 1200.00, 'Pedreiro'),
('10000000003', 'Lucas Souza', 30, '1994-05-20', 'M', 2, 'Ensino Médio', 800.00, 'Motorista'),
('10000000004', 'Mariana Souza', 28, '1996-07-10', 'F', 2, 'Ensino Superior', 0.00, 'Desempregada'),
('10000000005', 'Pedro Lima', 12, '2012-09-09', 'M', 3, '6º Ano', 0.00, 'Estudante'),
('10000000006', 'João Costa', 50, '1974-11-20', 'M', 4, 'Ensino Médio', 1000.00, 'Vigilante'),
('10000000007', 'Renata Rocha', 27, '1997-12-01', 'F', 5, 'Ensino Superior', 950.00, 'Professora'),
('10000000008', 'Laura Melo', 22, '2002-04-15', 'F', 6, 'Ensino Médio', 1500.00, 'Recepcionista'),
('10000000009', 'Mateus Dias', 45, '1979-02-18', 'M', 7, 'Ensino Fundamental', 700.00, 'Pedreiro'),
('10000000010', 'Camila Alves', 18, '2006-06-06', 'F', 8, '3º Ano', 0.00, 'Estudante');


INSERT INTO agente (nome, contato, login, senha) VALUES
('João Agente', 'joao@email.com', 'joao123', 'senha1'),
('Maria Agente', 'maria@email.com', 'maria123', 'senha2'),
('Pedro Agente', 'pedro@email.com', 'pedro123', 'senha3'),
('Ana Agente', 'ana@email.com', 'ana123', 'senha4'),
('Carlos Agente', 'carlos@email.com', 'carlos123', 'senha5'),
('Fernanda Agente', 'fer@email.com', 'fer123', 'senha6'),
('Lucas Agente', 'lucas@email.com', 'lucas123', 'senha7'),
('Juliana Agente', 'juliana@email.com', 'juliana123', 'senha8'),
('Rafael Agente', 'rafael@email.com', 'rafael123', 'senha9'),
('Paula Agente', 'paula@email.com', 'paula123', 'senha10');


INSERT INTO relatorio DEFAULT VALUES;
INSERT INTO relatorio DEFAULT VALUES;
INSERT INTO relatorio DEFAULT VALUES;
INSERT INTO relatorio DEFAULT VALUES;
INSERT INTO relatorio DEFAULT VALUES;
INSERT INTO relatorio DEFAULT VALUES;
INSERT INTO relatorio DEFAULT VALUES;
INSERT INTO relatorio DEFAULT VALUES;
INSERT INTO relatorio DEFAULT VALUES;
INSERT INTO relatorio DEFAULT VALUES;


INSERT INTO visita (idagente, idfamilia, idrelatorio, data, hora, status) VALUES
(1, 1, 1, '2024-07-01', '09:00', 'Realizada'),
(2, 2, 2, '2024-07-02', '10:00', 'Realizada'),
(3, 3, 3, '2024-07-03', '11:00', 'Cancelada'),
(4, 4, 4, '2024-07-04', '08:30', 'Pendente'),
(5, 5, 5, '2024-07-05', '14:00', 'Realizada'),
(6, 6, 6, '2024-07-06', '13:00', 'Realizada'),
(7, 7, 7, '2024-07-07', '15:00', 'Realizada'),
(8, 8, 8, '2024-07-08', '10:30', 'Cancelada'),
(9, 9, 9, '2024-07-09', '12:00', 'Realizada'),
(10, 10, 10, '2024-07-10', '09:30', 'Pendente');


INSERT INTO relatorio_observacoes (idrelatorio, observacoes) VALUES
(1, 'Família com boa organização.'),
(2, 'Necessidade de mais apoio financeiro.'),
(3, 'Casa em boas condições.'),
(4, 'Falta de saneamento básico.'),
(5, 'Família sem acesso à saúde.'),
(6, 'Moradia alugada.'),
(7, 'Boa estrutura familiar.'),
(8, 'Dificuldade de locomoção.'),
(9, 'Sem eletricidade.'),
(10, 'Família em situação de rua anterior.');


INSERT INTO relatorio_vacinacaoFamilia (idrelatorio, vacinacaoFamilia) VALUES
(1, 'Todos vacinados.'),
(2, 'Uma criança sem vacina.'),
(3, 'Atualização em dia.'),
(4, 'Vacinas atrasadas.'),
(5, 'Carteira de vacinação perdida.'),
(6, 'Vacinação parcial.'),
(7, 'Família recusou vacinação.'),
(8, 'Em processo de atualização.'),
(9, 'Sem dados.'),
(10, 'Recém-nascido vacinado.');


INSERT INTO relatorio_pesoFamilia (idrelatorio, pesoFamilia) VALUES
(1, 'Peso adequado.'),
(2, 'Desnutrição leve.'),
(3, 'Sobrepeso em adultos.'),
(4, 'Peso normal.'),
(5, 'Crianças abaixo do peso.'),
(6, 'Peso acima do ideal.'),
(7, 'Peso normal em todos.'),
(8, 'Sem pesagem.'),
(9, 'Peso crítico.'),
(10, 'Peso adequado.');


