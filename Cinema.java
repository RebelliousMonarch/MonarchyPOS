import java.util.Scanner;
public class Cinema {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);

// TODO 1: Make while loop for moviePicker so the system asks for a movie over and over until movie is selected
// TODO 1a: Curently moviePicker just prints "Invalid Selection" and ends the program

// TODO 2: Create userAuth object and add Admin/Customer types to it
// TODO 3: Allow admin to edit and maybe add movies/prices
// TODO 4: If movieTitle is an invalid selection reset ticketPice/ticketsPurchased to zero
    
        String companyName = "Monarchy Design Cinema";  // declare company name (easy to swap names)

        // declares and initialize variable for first and last names
        System.out.println("First name: ");  // ask for first name
        String firstName = keyboard.nextLine();  // user inputs firstName
        System.out.println("Last name: ");  // ask for last name
        String lastName = keyboard.nextLine();  // user inputs lastName

        // movie selection screen
        System.out.println("\nSelect movie:");  // print movie choices
        System.out.println("[1] Coraline\n[2] Pacific Rim\n[3] Breezed");
        System.out.println("[4] The Crow\n[5] Fantastic Mr. Fox\n[6] Isle of Dogs\n[7] Who's your Daddy");  // list movie choices pt. 2
        String movieTitle;  // declares empty string for movieTitle
        int moviePicker;  // declares empty integer for movieTitle switch case
        moviePicker = keyboard.nextInt();  // initializes moviePicker for user input

        switch(moviePicker){  // switch cases for movie slection
            case 1:
                movieTitle = "Coraline";
                break;
            case 2:
                movieTitle = "Pacific Rim";
                break;
            case 3:
                movieTitle = "Breezed";
                break;
            case 4:
                movieTitle = "The Crow";
                break;
            case 5:
                movieTitle = "Fantastic Mr. Fox";
                break;
            case 6:
                movieTitle = "Isle of Dogs";
                break;
            case 7:
                movieTitle = "Who's Your Daddy";
                break;
            default:
                movieTitle = "Invalid Selection";  // if user input is invalid, print as such
                break;
        }
        System.out.println("\nSelect viewing time:");  // print available viewing times
        System.out.println("[1] 2pm\n[2] 4pm\n[3] 6pm\n[4] 8pm\n[5] 10pm");
        String movieTime;  // declares empty string for movieTime
        int timePicker;  // declares empty integer for movieTime switch case
        timePicker = keyboard.nextInt();

        switch(timePicker){  // switch cases to pick viewing time
            case 1:
                movieTime = "2pm";
                break;
            case 2:
                movieTime = "4pm";
                break;
            case 3:
                movieTime = "6pm";
                break;
            case 4:
                movieTime = "8pm";
                break;
            case 5:
                movieTime = "10pm";
                break;
            default:
                movieTime = "Invalid Selection";  // if user input is invalid, print invalid
                break;
        }
        System.out.println("\nHow many tickets whould you like to purchase:");  // ask how many tickets purchased
        int ticketsPurchased = keyboard.nextInt();  // user inputs amount of tickets purchased

        // calculate cost and create username
        double ticketPrice = 11;  // declares standard ticket price
        double totalCost = (ticketPrice * ticketsPurchased) * 1.07;  // calculate and assign totalCost with (ticketPrice * ticketsPurchased)
        String username = firstName.toLowerCase() + lastName.toLowerCase();  // create username with first and last name in lowercase

        // print final screen
        System.out.println("_________________________________");
        System.out.println("\nUsername: " + username);
        System.out.println("Movie: " + movieTitle);
        System.out.println("Movie Time: " + movieTime);
        System.out.println("Number of Tickets: " + ticketsPurchased);
        System.out.println("Price per ticket: " + ticketPrice);
        System.out.println("Total price of " + ticketsPurchased + " tickets: " + totalCost);
        System.out.println("_________________________________");

        // thank user for using the system
        System.out.println("\nThank you for choosing " + companyName + " for your movie going experience.\nEnjoy your movie!\n");
        keyboard.close();  // close user input object to avoid memory leaks
    }
}