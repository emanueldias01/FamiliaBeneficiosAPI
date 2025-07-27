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



-- Inserir dados na tabela beneficio
INSERT INTO beneficio (nome, descricao, criterios, tipo, valor) VALUES
('Bolsa Família', 'Auxílio mensal para famílias de baixa renda', 'Renda familiar < 600', 'Mensal', 600.00),
('Vale Gás', 'Auxílio para compra de gás de cozinha', 'Famílias inscritas no CadÚnico', 'Bimestral', 120.00),
('Auxílio Educação', 'Ajuda de custo para estudantes', 'Famílias com estudantes matriculados', 'Mensal', 200.00),
('Cesta Básica', 'Distribuição mensal de alimentos', 'Famílias em extrema pobreza', 'Mensal', 300.00),
('Auxílio Saúde', 'Auxílio para compra de medicamentos', 'Comprovação de necessidade médica', 'Mensal', 150.00);

-- Inserir dados na tabela familia
INSERT INTO familia (nome, rua, numero, bairro, cidade, telefone, renda, numeroMembros) VALUES
('Família Silva', 'Rua das Flores', '123', 'Centro', 'Cidade A', '123456789', 500.00, 4),
('Família Souza', 'Av. Brasil', '456', 'Bela Vista', 'Cidade B', '987654321', 800.00, 5),
('Família Oliveira', 'Rua das Laranjeiras', '789', 'Jardim', 'Cidade A', '111222333', 400.00, 3),
('Família Costa', 'Rua Nova', '101', 'Vila Nova', 'Cidade C', '444555666', 300.00, 6),
('Família Lima', 'Rua Velha', '202', 'São José', 'Cidade B', '777888999', 1000.00, 4);

-- Inserir dados na tabela tem (família-benefício)
INSERT INTO tem (idfamilia, idbeneficio, dataInicio) VALUES
(1, 1, '2025-01-10'),
(2, 2, '2025-02-15'),
(3, 3, '2025-03-01'),
(4, 4, '2025-01-20'),
(5, 5, '2025-04-12');

-- Inserir dados na tabela pessoa
INSERT INTO pessoa (NIS, nome, idade, dataNascimento, genero, idfamilia, anoEscolar, renda, ocupacao) VALUES
('10000000001', 'João Silva', 35, '1990-01-01', 'M', 1, 'Ensino Médio', 150.00, 'Pedreiro'),
('10000000002', 'Maria Souza', 28, '1997-05-12', 'F', 2, 'Ensino Fundamental', 200.00, 'Diarista'),
('10000000003', 'Carlos Oliveira', 12, '2012-07-25', 'M', 3, '6º ano', 0.00, 'Estudante'),
('10000000004', 'Ana Costa', 40, '1985-11-30', 'F', 4, 'Ensino Médio', 300.00, 'Cozinheira'),
('10000000005', 'Pedro Lima', 65, '1960-03-10', 'M', 5, 'Analfabeto', 100.00, 'Aposentado');

-- Inserir dados na tabela agente
INSERT INTO agente (nome, contato, login, senha) VALUES
('Agente A', 'agentea@example.com', 'agentea', 'senha123'),
('Agente B', 'agenteb@example.com', 'agenteb', 'senha123'),
('Agente C', 'agentec@example.com', 'agentec', 'senha123'),
('Agente D', 'agented@example.com', 'agented', 'senha123'),
('Agente E', 'agentee@example.com', 'agentee', 'senha123');

-- Inserir dados na tabela relatorio
INSERT INTO relatorio DEFAULT VALUES;
INSERT INTO relatorio DEFAULT VALUES;
INSERT INTO relatorio DEFAULT VALUES;
INSERT INTO relatorio DEFAULT VALUES;
INSERT INTO relatorio DEFAULT VALUES;

-- Inserir dados na tabela visita (usando agentes, famílias e relatórios existentes)
INSERT INTO visita (idagente, idfamilia, idrelatorio, data, hora, status) VALUES
(1, 1, 1, '2025-06-01', '09:00:00', 'Concluída'),
(2, 2, 2, '2025-06-05', '10:30:00', 'Concluída'),
(3, 3, 3, '2025-06-10', '14:15:00', 'Concluída'),
(4, 4, 4, '2025-06-15', '16:00:00', 'Cancelada'),
(5, 5, 5, '2025-06-20', '08:45:00', 'Pendente');

-- Inserir dados na tabela relatorio_observacoes
INSERT INTO relatorio_observacoes (idrelatorio, observacoes) VALUES
(1, 'Família em situação vulnerável, sem emprego fixo.'),
(2, 'Crianças matriculadas na escola, mas sem transporte.'),
(3, 'Casa com estrutura precária, necessidade de reforma.'),
(4, 'Família com idoso doente, requer apoio médico.'),
(5, 'Família com boa organização, mas renda muito baixa.');

-- Inserir dados na tabela relatorio_vacinacaoFamilia
INSERT INTO relatorio_vacinacaoFamilia (idrelatorio, vacinacaoFamilia) VALUES
(1, 'Todos vacinados com esquema completo.'),
(2, 'Uma criança sem vacina contra sarampo.'),
(3, 'Vacinação da gripe pendente para dois membros.'),
(4, 'Nenhuma vacina registrada.'),
(5, 'Vacinas em dia conforme calendário.');

-- Inserir dados na tabela relatorio_pesoFamilia
INSERT INTO relatorio_pesoFamilia (idrelatorio, pesoFamilia) VALUES
(1, 'Peso normal para todos os membros.'),
(2, 'Uma criança abaixo do peso.'),
(3, 'Todos acima do peso recomendado.'),
(4, 'Peso não informado.'),
(5, 'Peso dentro da média para idade e altura.');

