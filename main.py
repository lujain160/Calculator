from calculator import Calculator
import time
import os


def main():
    mathimatice = Calculator("", "")

    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    while True:
        try:
            choice = input(
                "Choose Arithmetic Operation please:(+,-,*,/,%,//,**) or type exit "
            ).lower()
            if choice == "+":
                mathimatice.addition()

            #       ***************
            elif choice == "-":
                mathimatice.subtraction()

            #       ***************
            elif choice == "*":
                mathimatice.Multy()

            #       ***************
            elif choice == "/":
                mathimatice.division()

            #       ***************
            elif choice == "%":
                mathimatice.Module()

            #       ***************
            elif choice == "//":
                mathimatice.floor_division()

            #       ***************
            elif choice == "**":
                mathimatice.exponentiation()

            #       ***************
            elif choice == "exit":
                clear_screen()
                break

            else:
                print(
                    "Invalid choice! Please choose from Arithmetic Operation (+,-,*,/,%,//,**) and try again."
                )
                time.sleep(3)
                clear_screen()
                break
        except ValueError as ve:
            print(ve)
            time.sleep(2)
            clear_screen()
        except ZeroDivisionError:
            print("You connat divide by zero!!")
            time.sleep(2)
            clear_screen()
        except Exception as e:
            print(e)
            time.sleep(2)
            clear_screen()
        finally:
            print("task completed")
            time.sleep(1)
            clear_screen()


if __name__ == "__main__":
    main()
