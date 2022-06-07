def checkValidationn(entPhoneNumber,txtPhoneNumber):

    if len(entPhoneNumber.get()) > 11:
        txtPhoneNumber.set(txtPhoneNumber.get()[:len(txtPhoneNumber.get()) - 1])

    if len(entPhoneNumber.get()) >= 11:
        entPhoneNumber.config(highlightcolor='black')

    if not entPhoneNumber.get().isnumeric() and len(entPhoneNumber.get()) >= 1:
        txtPhoneNumber.set(txtPhoneNumber.get()[:len(txtPhoneNumber.get()) - 1])
