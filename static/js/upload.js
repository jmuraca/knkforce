window.onload = function() 
{	
    $('#upload-file-btn').click(function() {
        var form_data = new FormData($('#upload-file')[0]);
        $.ajax({
            type: 'POST',
            url: '/uploadajax',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: false,
            success: function(data) 
			{
				d = new Date();
                $('#image_preview img').attr("src", "svg/pattern.svg?"+d.getTime());
            },
        });
    });
	
	$('.direction').click(function() 
	{
		var direction =  $(this).attr('data-direction');
		$.ajax({
			type: "GET",
			url: "/move",
			data: "direction="+direction,
			success: function(msg)
			{
				console.log(direction);
			}
		});
		return false; // prevent default
    });
	
	$('.cut').click(function() 
	{
		$.ajax({
			type: "POST",
			url: "/cut",
			success: function(msg)
			{
				console.log("finished");
			}
		});
		return false; // prevent default
    });
}