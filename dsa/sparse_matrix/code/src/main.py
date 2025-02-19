from sparse_matrix import CompressedMatrix

if __name__ == "__main__":
    try:
        print("Choose an operation to perform:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4 for Fetching a value")
        user_choice = int(input("Enter the number of the operation (1/2/3): "))
       
        
        file1_path = input("Provide first matrix file path: ")
        file2_path = input("Provide second matrix file path: ")
        
        matrix_a = CompressedMatrix(file1_path)
        matrix_b = CompressedMatrix(file2_path)
        
        if user_choice == 1:
            outcome = matrix_a.combine(matrix_b)
        elif user_choice == 2:
            outcome = matrix_a.subtract(matrix_b)
        elif user_choice == 3:
            outcome = matrix_a.multiply(matrix_b)
        elif user_choice == 4:
            row_val = int(input("Specify row: "))
            col_val = int(input("Specify column: "))
            file_selection = int(input("Select matrix (1 or 2): "))
            
            if file_selection == 1:
                outcome = matrix_a.fetch_value(row_val, col_val)
            elif file_selection == 2:
                outcome = matrix_b.fetch_value(row_val, col_val)
            else:
                outcome = matrix_a.fetch_value(row_val, col_val)
        else:
            raise ValueError("Invalid selection")
        
        print("Output:")
        print(outcome)
        
    except Exception as error:
        print(f"Error encountered: {error}")