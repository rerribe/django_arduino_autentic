Esse projeto é tentativa de reprodução de um sistema que utiliza um sensor RFID(tag ou cartão de identificação) 
para registrar frequencia, prover e registrar acesso(fechaduras eletronicas), assim como registrar novos usuários.

- Um ponto interessante é a captura de uma escrita feitar pelo arduino na porta serial do sistema que completa o
formulário do front-end na página de registro de novos usuários. 

- Uma coisa que tenho em mente é a menor utilização de recursos de terceiros possível, logo, tento não instalar pacotes
e criar as funções.

- a leitura de serial é feita por um código em C, que utiliza bibliotecas do sistema e código embarcado para a leitura.
(O uso de flags é muito legal).

Inserção acontece, porém por meio de testes realizados com o Postman, é visto que a string criada pelo front-end não é aceita pelo JSONParser do RESTApi, então:

- próximo passo é tratar a requisição para um formato aceito pelo JSONParser
