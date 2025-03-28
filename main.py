from sparse_matrix import CompressedMatrix

if __name__ == "__main__":
    try:
        print("Choose an operation to perform:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        user_choice = int(input("Enter the number of the operation (1/2/3): "))
       
        operations = ["", "addition", "subtraction", "multiplication"]
        
        if user_choice == 1:
            matrix_a = CompressedMatrix('./sample_inputs/easy_sample_02_1.txt')
            matrix_b = CompressedMatrix('./sample_inputs/easy_sample_02_2.txt')
            outcome = matrix_a.combine(matrix_b)
        elif user_choice == 2:
            matrix_a = CompressedMatrix('./sample_inputs/easy_sample_02_1.txt')
            matrix_b = CompressedMatrix('./sample_inputs/easy_sample_02_2.txt')
            outcome = matrix_a.subtract(matrix_b)
        elif user_choice == 3:
            matrix_a = CompressedMatrix('./sample_inputs/easy_sample_02_1.txt')
            matrix_b = CompressedMatrix('./sample_inputs/easy_sample_02_3.txt')
            outcome = matrix_a.multiply(matrix_b)
        else:
            raise ValueError("Invalid selection")
        
        output_path = f'./results/result_{operations[user_choice]}.txt'
        print("Saving file to : ", output_path)
        with open(output_path, 'w+') as file:
            file.write(str(outcome))
        
    except Exception as error:
        print(f"Error encountered: {error}")
