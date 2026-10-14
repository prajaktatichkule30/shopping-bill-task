// Name: Prajakta Tichkule
// Program: Shopping Bill
// Task: 01
// Language: Java

public class ShoppingBill
    {
public static void main(String[] args) 
        {
System.out.println("Welcome to Shopping Bill System");
System.out.println("--------------------------------");
// Sample values
        double a = 100;
        double b = 100;
        double c = 100;
        double d = 100;
        double e = 100;
 // Call the main calculation method
calculateDiscountedBill(a, b, c, d, e);
    }
// Calculate electronics amount with 18% GST
 static double calculateElectronicsGST(double a, double b) 
{
double amount = a + b;
double gst = amount * 18 / 100;
 double total = amount + gst;
 return total;
    }
// Calculate fashion amount with 13% GST
    static double calculateFashionGST(double c, double d) 
{
 double amount = c + d;
double gst = amount * 13 / 100;
double total = amount + gst;
 return total;
    }
 // Calculate food amount with 7% GST
    static double calculateFoodGST(double e) {
double gst = e * 7 / 100;
double total = e + gst;
 return total;
    }
// Calculate total bill after GST
    static double totalBill(double a, double b, double c, double d, double e)
{
double electronics = calculateElectronicsGST(a, b);
double fashion = calculateFashionGST(c, d);
double food = calculateFoodGST(e);
 double total = electronics + fashion + food;

 return total;
    }

// Calculate discount and final bill
 static double calculateDiscountedBill(double a, double b, double c, double d, double e) {

 double total = totalBill(a, b, c, d, e);

        double discount = total * 20 / 100;
        double finalAmount = total - discount;

        System.out.println("\n----------- Shopping Bill -----------");

        System.out.printf("Total after GST       : %.2f%n", total);
        System.out.printf("Discount (20%%)        : %.2f%n", discount);
        System.out.printf("Final payable amount  : %.2f%n", finalAmount);

        System.out.println("------------------------------------");
        System.out.println("Thank you for shopping!");

        return finalAmount;
    }
}
