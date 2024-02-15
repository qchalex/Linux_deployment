class GetSidebarElementsValue:
    @staticmethod
    def get_sidebar_value(value, element):
        if element == "gender":
            if value == 1:
                return 'Male'
            elif value == 2:
                return 'Female'
        elif element == "senior_citizen":
            if value == 1:
                return 0
            elif value == 2:
                return 1
        elif element == "phone_service":
            if value == 1:
                return 'Yes'
            elif value == 2:
                return 'No'
        elif element == "internet_service":
            if value == 1:
                return 'DSL'
            elif value == 2:
                return 'Fiber optic'
            elif value == 3:
                return 'No'
        elif element == "payment_method":
            if value == 1:
                return 'Bank transfer (automatic)'
            elif value == 2:
                return 'Mailed check'
            elif value == 3:
                return 'Credit card (automatic)'
            elif value == 4:
                return 'Electronic check'
        elif element == "contract":
            if value == 1:
                return 'Month-to-Month'
            elif value == 2:
                return 'One year'
            elif value == 3:
                return 'Two year'
