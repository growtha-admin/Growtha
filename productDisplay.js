const productDisplay = document.getElementById('product_display');

const productDialog = document.getElementById('product_dialog_main')
const openproductDialog = document.getElementById('open_productDialog')
const closeproductDialog = document.getElementById('close_productDialog')


const overlay = document.getElementById('overlay')

let productDisplaydata




fetch('products.json')
    .then(response => response.json())
    .then(data => {
        productDisplaydata = data;

        data.forEach(product => {
            const productDiv = document.createElement('div');
            productDiv.classList.add('product');

            productDiv.innerHTML =
                `
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
                        </p>
                        <p class="product_desc">${product.description}</p>
                        <div class="product_details">
                            <p class="price">${product.price}</p>
                            <a href="${product.url}" target="_blank" rel="noopener noreferrer" class="btn product_homebtn" id="product_homebtn">View Details</a>
                        </div>
                    </div>
                `
            ;

            productDisplay.appendChild(productDiv);
        });


        
        
    })
    .catch(error => {
        console.log('Error:', error);
        productDisplay.innerHTML = 'Error: ' + error;
    });


function displayproductDialog() {
    openproductDialog.addEventListener('click', (e) => {
        e.preventDefault()

        console.log(e)
    
        productDialog.showModal()
        document.body.classList.add('station_body')
        overlay.style.display('block')                                    
    })
    
    closeproductDialog.addEventListener('click', () => {
        productDialog.close();
        document.body.classList.remove('station_body')
        overlay.style.display = 'none'  
    })
}

// openproductDialog.forEach((container) => {
//     console.log(container)
//     container.addEventListener('click', () => {
//         if (productDisplaydata){
//             const { type, description } = product
//         }
//     })
// })


// ProductQueryParameterMatch();

// displayproductDialog()

// productDialogContent()

// window.addEventListener('load', openproductDialogIQPM)


function ProductQueryParameterMatch() {
    const urlParam = new URLSearchParams(window.location.search);
    console.log(urlParam)
    const productParam = urlParam.get('product');
    console.log(productParam)

    if (productParam) {
        fetch('products.json')
        .then(response => response.json())
        .then(data => {
            
            
            const productDesc = document.getAnimations('product_desc')
            productDesc.textContent = JSON.stringify(data)


    
            console.log(productDesc.textContent)


            productDialog.showModal()
        })
        .catch(error => {
            console.log('Wahala', error)
        })
    } else {
        console.log('Query error')
    }
}

openproductDialog.addEventListener('click', (e) => {
    e.preventDefault()


})

