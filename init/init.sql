-- Tabela: beneficio
CREATE TABLE beneficio (
    idBeneficio SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    descricao TEXT,
    criterios TEXT,
    tipo VARCHAR(50),
    valor NUMERIC(10, 2)
);

-- Tabela: familia
CREATE TABLE familia (
    idFamilia SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    rua VARCHAR(100),
    numero VARCHAR(10),
    bairro VARCHAR(50),
    cidade VARCHAR(50),
    telefone VARCHAR(20),
    renda NUMERIC(10, 2),
    numeroMembros INT
);

-- Tabela: tem (relação entre família e benefício)
CREATE TABLE tem (
    idFamilia INT REFERENCES familia(idFamilia),
    idBeneficio INT REFERENCES beneficio(idBeneficio),
    dataInicio DATE,
    PRIMARY KEY (idFamilia, idBeneficio)
);

-- Tabela: pessoa
CREATE TABLE pessoa (
    NIS BIGINT PRIMARY KEY,
    nome VARCHAR(100),
    idade INT,
    dataNascimento DATE,
    genero CHAR(1),
    idFamilia INT REFERENCES familia(idFamilia)
);

-- Tabela: menorIdade
CREATE TABLE menorIdade (
    NIS BIGINT PRIMARY KEY REFERENCES pessoa(NIS),
    anoEscolar VARCHAR(20)
);

-- Tabela: maiorIdade
CREATE TABLE maiorIdade (
    NIS BIGINT PRIMARY KEY REFERENCES pessoa(NIS),
    renda NUMERIC(10, 2),
    ocupacao VARCHAR(100)
);

-- Tabela: agente
CREATE TABLE agente (
    idAgente SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    contato VARCHAR(100),
    login VARCHAR(50),
    senha VARCHAR(100)
);

-- Tabela: relatorio
CREATE TABLE relatorio (
    idRelatorio SERIAL PRIMARY KEY
);

-- Tabela: visita
CREATE TABLE visita (
    idAgente INT REFERENCES agente(idAgente),
    idRelatorio INT REFERENCES relatorio(idRelatorio),
    data DATE,
    hora TIME,
    status VARCHAR(50),
    PRIMARY KEY (idAgente, idRelatorio)
);

-- Tabela: relatorio_observacoes
CREATE TABLE relatorio_observacoes (
    observacoes TEXT,
    idRelatorio INT PRIMARY KEY REFERENCES relatorio(idRelatorio)
);

-- Tabela: relatorio_vacinacaoFamilia
CREATE TABLE relatorio_vacinacaoFamilia (
    vacinacaoFamilia TEXT,
    idRelatorio INT PRIMARY KEY REFERENCES relatorio(idRelatorio)
);

-- Tabela: relatorio_pesoFamilia
CREATE TABLE relatorio_pesoFamilia (
    pesoFamilia TEXT,
    idRelatorio INT PRIMARY KEY REFERENCES relatorio(idRelatorio)
);
