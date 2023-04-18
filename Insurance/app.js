// Selectors
const policyForm = document.getElementById('policy-form');
const policyTable = document.getElementById('policy-table');
const errorMessage = document.getElementById('error-message');

// Event Listeners
policyForm.addEventListener('submit', createPolicy);

// Functions
function createPolicy(e) {
    e.preventDefault();

    // Get form values
    const policyNumber = document.getElementById('policy-number').value;
    const policyType = document.getElementById('policy-type').value;
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;
    const premium = document.getElementById('premium').value;

    // Validate form
    if (!policyNumber || !policyType || !startDate || !endDate || !premium) {
        errorMessage.textContent = 'Please fill in all fields.';
        return;
    }

    // Create policy object
    const policy = {
        policyNumber,
        policyType,
        startDate,
        endDate,
        premium
    };

    // Add policy to table
    addPolicyToTable(policy);

    // Clear form
    policyForm.reset();
}

function addPolicyToTable(policy) {
    const row = policyTable.insertRow(-1);
    const policyNumberCell = row.insertCell(0);
    const policyTypeCell = row.insertCell(1);
    const startDateCell = row.insertCell(2);
    const endDateCell = row.insertCell(3);
    const premiumCell = row.insertCell(4);

    policyNumberCell.textContent = policy.policyNumber;
    policyTypeCell.textContent = policy.policyType;
    startDateCell.textContent = policy.startDate;
    endDateCell.textContent = policy.endDate;
    premiumCell.textContent = policy.premium;
}

// Add cancel button
const cancelButton = document.createElement('button');
cancelButton.textContent = 'Cancel';
cancelButton.addEventListener('click', function() {
    const reason = prompt('Enter reason for cancellation:');
    if (reason) {
        const cancellationDate = new Date().toLocaleDateString();
        policy.status = 'cancelled';
        statusCell.textContent = policy.status;
        cancelCell.textContent = `${reason} (${cancellationDate})`;
        cancelButton.disabled = true;
    }
});
cancelCell.appendChild(cancelButton);