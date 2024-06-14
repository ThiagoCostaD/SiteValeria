function my_scope() {
    const form = document.querySelectorAll('.form-delete');

    for (const form of forms) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            const confirmation = confirm('Are you sure you want to delete this?');

            if (confirmation) {
                form.submit();
            }
        });
    }
}

my_scope();