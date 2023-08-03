const productDisplay = document.getElementById('product_display');



fetch('products.json')
.then(response => response.json())
.then(data => {

  // Iterate over each object in the JSON array
  data.forEach(product => {

    // Create a div element to display the data
    const productDiv = document.createElement('div');
    productDiv.classList.add('product');
    
    // Populate the div with the object's data
    productDiv.innerHTML = `
      <div class="product_content">                                                            
        <div class="product_image_div">
            <img class="product_image" src="${product.image}" alt="${product.imagealttext}">
        </div>                                                    
      <div class="product_content_text">                                                                    
        <span class="product_type">${product.type}</span>                                                                       
        <h3 class="product_title">${product.title}</h3>            
        <p class="creator_name_wrapper">
          By 
          <strong class="creator_name">${product.creatorname}</strong>
          <div class="creator_details_wrapper">
            <div>
              <div class="creator_biodetails">
                <img class="creator_image" src="${product.creatorimage}" alt="${product.creatorname}">
                <p class="details_creator_name">${product.creatorname}</p>
              </div>
              <hr class="hr_cdw">
              <p class="details_creator_desc">${product.creatordesc}</p>
            </div>
          </div>
        </p>            
        <p class="product_desc">${product.description}</p>                                                            
        <div class="product_details">
            <p class="price">${product.price}</p>                                                                    
            <a href="${product.url}" target="_blank" rel="noopener noreferrer" class="btn product_homebtn" id="product_homebtn">View Details</a>
        </div>
      </div>
    `;
    
    // Append the div to the data container
    productDisplay.appendChild(productDiv);
  });
})

.catch(error => {  
    console.log('Error:', error);
    productDisplay.innerHTML = 'Error: ' + error;
});