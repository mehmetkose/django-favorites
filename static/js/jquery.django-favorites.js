$(function(){
	$('a.favIt').live('click', function(){		
		var itemId = $(this).attr('id').split("_")[1];
		$.ajax({
			type: "POST",
			url: $(this).attr("href"),
			data: {},
			dataType: "json",
			timeout: 2000,
			cache: false,			
			beforeSend: function(XMLHttpRequest) {
				//$("#loader").fadeIn();
			},
			error: function(data, XMLHttpRequest, textStatus, errorThrown){
				$(this).html("Error connecting to the server.");
			},              
			complete: function(XMLHttpRequest, textStatus) {
				//$("#loader").fadeOut();
			},                        
			success: function(data, textStatus, XMLHttpRequest){
				$('#FavIt_'+itemId).html(data.message);
				$('#FavCounter_'+itemId).html(data.counter);
			}
			});				
		return false;
	});
});