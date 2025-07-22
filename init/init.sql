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
