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
	
	$('.command').click(function() 
	{
		var url = this.href;
		var attributes = $(this).data();
		$.ajax({
			type: "POST",
			url: url,
			data: attributes,
			success: function(msg)
			{
				console.log("ok");
			}
		});
		return false; // prevent default

		
		
		console.log(attributes);
    });
}