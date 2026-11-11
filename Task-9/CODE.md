### Problem Statement:
 Retail Billing with Multiple Discount Rules: Process multiple products, quantities, categoryspecific taxes, threshold discounts, and maximum concession limits to generate an itemized invoice. 
 
### Algorithm:
1. Start
2. Read number of products
3. For each product, read name, category, price, quantity
4. Calculate Subtotal = Price * Quantity
5. Calculate Tax based on category
6. Total = Subtotal + Tax
7. Add Total to Grand Total
8. After all products, check discount rule
9. If discount > 500, set discount = 500
10. Final = Grand Total - Discount
11. Display invoice
12. Stop

### Flowchart:
```mermaid
flowchart TD
    A[Start] --> B[Read number of products]
    B --> C[Read product name, category, price, qty]
    C --> D[Subtotal = Price * Qty]
    D --> E{Category?}
    E -- Electronics --> F[Tax = 18%]
    E -- Grocery --> G[Tax = 5%]
    E -- Clothing --> H[Tax = 12%]
    F --> I[Total = Subtotal + Tax]
    G --> I
    H --> I
    I --> J[Grand Total = Grand Total + Total]
    J --> K{More Products?}
    K -- Yes --> C
    K -- No --> L{Grand Total > 5000?}
    L -- Yes --> M[Discount = 10%]
    L -- No --> N{Grand Total > 2000?}
    N -- Yes --> O[Discount = 5%]
    N -- No --> P[Discount = 0]
    M --> Q{Discount > 500?}
    O --> Q
    P --> Q
    Q -- Yes --> R[Discount = 500]
    Q -- No --> S[Keep Discount]
    R --> T[Final = Grand Total - Discount]
    S --> T
    T --> U[Display Invoice]
    U --> V[Stop]
```

### Sample Input:
Enter number of products: 2

Enter product name: Rice
Enter category (Electronics/Grocery/Clothing): Grocery
Enter price: 100
Enter quantity: 10

Enter product name: Shirt
Enter category (Electronics/Grocery/Clothing): Clothing
Enter price: 1000
Enter quantity: 2

### Sample Output:
Rice: Subtotal 1000.0, Tax 50.0, Total 1050.0
Shirt: Subtotal 2000.0, Tax 240.0, Total 2240.0

 Invoice 
Grand Total: 3290.0
Discount: 164.5
Final Payable: 3125.5
