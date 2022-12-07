console.log('teste do console')

const troca_valor = document.getElementById('cartao');
console.log(troca_valor.value)

const btn = document.querySelector("button");

btn.addEventListener("click", function() {

	$.ajax({
		type:'GET',
		url: 'resposta_arduino',
		success: function(response){
			troca_valor.value = response.chave
			console.log(response.chave)
			console.log('ae, mto bem')
		},
		error: function(error){
			console.log('erro',error)
		}
	})
	
});



