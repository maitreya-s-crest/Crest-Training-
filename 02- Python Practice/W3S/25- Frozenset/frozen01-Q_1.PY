def main():
    emp1 = {"name": "Maitreya Sapariya", "age": 21, "country": "Finland"}
    emp2 = {"name": "Aditi", "age": 22, "country": "India"}

    employees_data = {
        frozenset(emp1.items()): emp1,
        frozenset(emp2.items()): emp2,
    }
    
    for key, value in employees_data.items():
        print("Key:", key)
        print("Value:", value)
        print()

if __name__ == "__main__":
    main()
