class CompressedMatrix:
    def __init__(self, file_source=None, row_count=0, col_count=0):
        self.file_source = file_source  # The file to read
        self.total_rows = row_count
        self.total_cols = col_count
        self.data_points = {}  # Dictionary to store non-zero values as {(row, col): value}
        
        if file_source:
            self.extract_data(file_source)

    def extract_data(self, file_source):
        try:
            with open(file_source, 'r') as f:
                content = f.readlines()
            
            self.total_rows = int(content[0].split('=')[1].strip())
            self.total_cols = int(content[1].split('=')[1].strip())
            
            for entry in content[2:]:
                entry = entry.strip()
                if not entry:
                    continue
                
                if not (entry.startswith('(') and entry.endswith(')')):
                    raise ValueError('Incorrect file format')
                
                row, col, val = map(int, entry[1:-1].split(','))
                self.data_points[(row, col)] = val
        
        except Exception as err:
            raise ValueError(f"File read error: {err}")
    
    def fetch_value(self, row, col):
        return self.data_points.get((row, col), 0)
    
    def modify_value(self, row, col, val):
        if val != 0:
            self.data_points[(row, col)] = val
        elif (row, col) in self.data_points:
            del self.data_points[(row, col)]
    
    def combine(self, other):
        outcome = CompressedMatrix(row_count=max(self.total_rows, other.total_rows),
                                   col_count=max(self.total_cols, other.total_cols))
        
        for (row, col), val in self.data_points.items():
            if (row, col) in other.data_points:
                outcome.modify_value(row, col, val + other.fetch_value(row, col))
        return outcome
    
    def subtract(self, other):
        outcome = CompressedMatrix(row_count=max(self.total_rows, other.total_rows),
                                   col_count=max(self.total_cols, other.total_cols))
        
        for (row, col), val in self.data_points.items():
            if (row, col) in other.data_points:
                outcome.modify_value(row, col, val - other.fetch_value(row, col))
        return outcome
    
    def multiply(self, other):
        if self.total_cols != other.total_rows:
            raise ValueError("Invalid dimensions for multiplication")
        
        outcome = CompressedMatrix(row_count=self.total_rows, col_count=other.total_cols)
        
        for (row, col), val in self.data_points.items():
            for k in range(other.total_cols):
                if (col, k) in other.data_points:
                    outcome.modify_value(row, k, outcome.fetch_value(row, k) + val * other.fetch_value(col, k))
        
        return outcome
    
    def __str__(self):
        items = [f"({row}, {col}, {val})" for (row, col), val in self.data_points.items()]
        return f"CompressedMatrix({self.total_rows}x{self.total_cols}):\n" + "\n".join(items)