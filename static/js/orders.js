$(document).ready(function () {
    const productCheckboxes = document.querySelectorAll('#product-checkbox');
    const deleteButtons = document.querySelectorAll("#delete-product");
    [0, 1].forEach((index) => {
        // deleteButtons[index].prop("disabled", true);
        productCheckboxes[index].addEventListener('click', function () {
            if (productCheckboxes[index].checked) {
                alert('Checked!')
                deleteButtons[index].attr("disabled", false);
            } else {
                alert('Unchecked!')
                deleteButtons[index].attr("disabled", true);
            }
        });
    })
    // $("#delete-product").attr("disabled", true);
    // $("#product-checkbox").click(function () {
    //     if(this.checked){
    //         $("#delete-product").attr("disabled", false);
    //     } else{
    //         $("#delete-product").attr("disabled", true);
    //     }
    // });
});