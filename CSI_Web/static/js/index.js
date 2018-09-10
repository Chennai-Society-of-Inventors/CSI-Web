function isEmpty(field) {
    if(field === '' || field === undefined) {
        return true;
    }
    return false;
}

function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

function validateMobileNumber(mobileNumber) {
    var numberCount = 0;
    for(var i = 0; i < mobileNumber.length; i++) {
        if(mobileNumber[i] >= "0" && mobileNumber[i] <= "9") {
            ++numberCount;
        }
    }
    if(numberCount === 10 && mobileNumber.length === 10) {
        return true;
    }
    return false;
}

function submitProblem(e){
    var problemCategory = document.getElementById("problemCategory").value;
    var problemDescription = document.getElementById("problemDescription").value;
    var name = document.getElementById("name").value;
    var contactNumber = document.getElementById("contactNumber").value;
    var contactAddress = document.getElementById("contactAddress").value;
    var emailID = document.getElementById("emailId").value;
    if(isEmpty(problemCategory) || isEmpty(problemDescription) || isEmpty(name) || isEmpty(contactNumber) ||
        isEmpty(contactAddress) || isEmpty(emailID)) {
        toastr.error('No field should be empty!');
        return;
    }
    if(!validateEmail(emailID)) {
        toastr.error('Enter a proper Email ID!');
        return;
    }
    if(!validateMobileNumber(contactNumber)) {
        toastr.error('Enter a proper Mobile Number!');
        return;
    }
    $.ajax({
        data: {'problemCategory':problemCategory,
            'problemDescription':problemDescription,
            'name': name,
            'contactNumber': contactNumber,
            'contactAddress': contactAddress,
            'emailID': emailID},
        url: '/submit_problem',
        type: 'POST',
        success: function (data) {
            toastr.success(data["success"]);
            $("#problemModal").modal("hide");
        },
        error: function () {
            toastr.error(data["error"]);
        }
    });
}

function submitInvention(e){
    var invention = document.getElementById("invention").value;
    var problemDescription = document.getElementById("inventionProblemDescription").value;
    var team = document.getElementById("teamDetails").value;
    var contactNumber = document.getElementById("inventorContactNumber").value;
    var emailID = document.getElementById("inventorEmailId").value;
    if(isEmpty(invention) || isEmpty(problemDescription) || isEmpty(contactNumber) ||
        isEmpty(team) || isEmpty(emailID)) {
        toastr.error('No field should be empty!');
        return;
    }
    if(!validateEmail(emailID)) {
        toastr.error('Enter a proper Email ID!');
        return;
    }
    if(!validateMobileNumber(contactNumber)) {
        toastr.error('Enter a proper Mobile Number!');
        return;
    }
    $.ajax({
        data: {'invention':invention,
            'problemDescription':problemDescription,
            'team': team,
            'contactNumber': contactNumber,
            'emailID': emailID},
        url: '/submit_invention',
        type: 'POST',
        success: function (data) {
            toastr.success(data["success"]);
            $("#solutionModal").modal("hide");
        },
        error: function () {
            toastr.error(data["error"]);
        }
    });
}