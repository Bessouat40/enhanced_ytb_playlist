
function createPlaylistCard(playlistData){

			let playlistDescription = playlistData['description'].split('.');
			let playlistViews = playlistData['vues'].replace('vues','');
			let playlistFormattedViews = parseInt(playlistViews).toLocaleString();
			let playlistId = playlistData['_id'];
			let playlistTitle = playlistData['playlist'];
			let playlistImgUrl = playlistData['url_img'];
			let playlistNbVideos = playlistData['nbr_videos'];
			let playlistDuration = playlistData['playlist_duration'];

			let htmlString = `
		  				<div class="row justify-content-center"> 		  					
		  					<div class="col-md-10 card mb-3 mt-2 border-0 rounded shadow-sm">

				  				<h5 class="card-title mt-1 mb-2">${playlistTitle} </h5> 
				  				
				  				<div class="row mb-2 justify-content-center">

				  					<div class="col-md-4 pr-3">
				  						<img src="${playlistImgUrl}"  class="rounded border"  style="width: 14rem;">
				  					</div>
				  					
				  					<div class="col-md-2 my-auto">
					  					<p class="text-center align-middle h3" >${playlistFormattedViews} <i class="material-icons">&#xe8f4;</i></p>					  							
				  					</div>

				  					<div class="col-md-2 my-auto">
				  						<p class="text-center align-middle h3" >${playlistNbVideos} <i class="material-icons">video_library</i></p>
				  					</div>

				  					<div class="col-md-2 my-auto">
				  						<p class="text-center align-middle h3" >${playlistDuration} <i class="material-icons">schedule </i></p>
				  					</div>

				  					<a href="/p/${playlistId}" class="stretched-link"></a>
			  					</div>
			  			
		  					</div>
		  				</div>`

		  				var div = document.createElement('div');
						div.innerHTML = htmlString.trim();
			return(div)
	}


function createShortPlaylistCard(playlistData){

		let imgUrl = playlistData['url_img'];
		let playlistId = playlistData['_id'];
		let playlistTitle = playlistData['playlist'];

		var newCard = document.createElement("div");
		newCard.className = 'col-md-3 p-2 mt-2';
		newCard.innerHTML = `
			<div class="card">
				<img class="card-img-top" src="${imgUrl}" alt="Card image cap">
				<div class="card-body">
					<p class="card-text">${playlistTitle}</p>
				</div>
				<a href="/p/${playlistId}" class="stretched-link"></a>
			</div>
		`
		return(newCard)
	}
