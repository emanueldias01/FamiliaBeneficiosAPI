-- Tabela: beneficio
CREATE TABLE beneficio (
    idBeneficio SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT NOT NULL,
    criterios TEXT NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    valor NUMERIC(10, 2) NOT NULL CHECK (valor >= 0)
);

-- Tabela: familia
CREATE TABLE familia (
    idFamilia SERIAL PRIMARY KEY,
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
    idFamilia INT,
    idBeneficio INT,
    dataInicio DATE,
    PRIMARY KEY (idFamilia, idBeneficio),
    FOREIGN KEY (idFamilia) REFERENCES familia(idFamilia) ON DELETE CASCADE,
    FOREIGN KEY (idBeneficio) REFERENCES beneficio(idBeneficio) ON DELETE CASCADE
);

-- Tabela: pessoa
CREATE TABLE pessoa (
    NIS VARCHAR(11) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    dataNascimento DATE NOT NULL,
    genero CHAR(1),
    idFamilia INT,
    anoEscolar VARCHAR(20),
    renda NUMERIC(10,2) NOT NULL CHECK (renda >= 0),
    ocupacao VARCHAR(100)
    FOREIGN KEY (idFamilia) REFERENCES familia(idFamilia) ON DELETE CASCADE
);

-- Tabela: agente
CREATE TABLE agente (
    idAgente SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    contato VARCHAR(100) NOT NULL,
    login VARCHAR(50) NOT NULL,
    senha VARCHAR(100) NOT NULL
);

-- Tabela: relatorio
CREATE TABLE relatorio (
    idRelatorio SERIAL PRIMARY KEY
);

-- Tabela: visita
CREATE TABLE visita (
    idAgente INT,
    idFamilia INT
    idRelatorio INT,
    data DATE,
    hora TIME NOT NULL,
    status VARCHAR(50) NOT NULL,
    PRIMARY KEY (idAgente, idRelatorio),
    FOREIGN KEU (idFamilia) REFERENCES familia(idFamilia) ON DELETE CASCADE,
    FOREIGN KEY (idAgente) REFERENCES agente(idAgente) ON DELETE CASCADE,
    FOREIGN KEY (idRelatorio) REFERENCES relatorio(idRelatorio) ON DELETE CASCADE
);

-- Tabela: relatorio_observacoes
CREATE TABLE relatorio_observacoes (
    observacoes TEXT NOT NULL,
    idRelatorio INT PRIMARY KEY,
    FOREIGN KEY (idRelatorio) REFERENCES relatorio(idRelatorio) ON DELETE CASCADE
);

-- Tabela: relatorio_vacinacaoFamilia
CREATE TABLE relatorio_vacinacaoFamilia (
    vacinacaoFamilia TEXT NOT NULL,
    idRelatorio INT PRIMARY KEY,
    FOREIGN KEY (idRelatorio) REFERENCES relatorio(idRelatorio) ON DELETE CASCADE
);

-- Tabela: relatorio_pesoFamilia
CREATE TABLE relatorio_pesoFamilia (
    pesoFamilia TEXT NOT NULL,
    idRelatorio INT PRIMARY KEY,
    FOREIGN KEY (idRelatorio) REFERENCES relatorio(idRelatorio) ON DELETE CASCADE
);
