window.onload = function() 
{	
	var file_input = document.getElementById('file_input');
	
	file_input.addEventListener('change', function(e) 
	{
		var file = file_input.files[0];
		var image_type = /image.*/;

		if (file.type.match(image_type)) 
		{
			var reader = new FileReader();

			reader.onload = function(e) 
			{
				var img = new Image();
				img.src = reader.result;
				
				//fileDisplayArea.appendChild(img);
				
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
			}

			reader.readAsDataURL(file);	
		} 
		else
		{
			fileDisplayArea.innerHTML = "File not supported!"
		}
	});
	
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