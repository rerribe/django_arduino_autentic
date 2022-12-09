Esse projeto é tentativa de reprodução de um sistema que utiliza um sensor RFID(tag ou cartão de identificação) 
para registrar frequencia, prover e registrar acesso(fechaduras eletronicas), assim como registrar novos usuários.

- Um ponto interessante é a captura de uma escrita feitar pelo arduino na porta serial do sistema que completa o
formulário do front-end na página de registro de novos usuários. 

- Uma coisa que tenho em mente é a menor utilização de recursos de terceiros possível, logo, tento não instalar pacotes
e criar as funções.

- a leitura de serial é feita por um código em C, que utiliza bibliotecas do sistema e código embarcado para a leitura.
(O uso de flags é muito legal).

- próximo passo é a implementação do CRUD.
