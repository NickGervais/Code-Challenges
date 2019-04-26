package main

import (
    "fmt"
    "sort"
    "math"
)

// make costs global so sort functions can use the values
var g_costs [][]int

// Set up sorting functions by city cost difference
type byCityCost [][]int

func (arr byCityCost) Len() int {
    return len(arr)
}

// we are sorting based off the difference between cost of city A and B
func (arr byCityCost) Less(i, j int) bool {
    i_vals := g_costs[arr[i][0]]
    j_vals := g_costs[arr[j][0]]
    return math.Abs(float64(i_vals[0]-i_vals[1])) < math.Abs(float64(j_vals[0]-j_vals[1]))
}

func (arr byCityCost) Swap(i, j int) {
    arr[i], arr[j] = arr[j], arr[i]
}

// main solution function
func twoCitySchedCost(costs [][]int) int {
    g_costs = costs
    taken := make([][]int, len(costs))
    to_a := 0
    to_b := 0
    
    // First take the min between city A and B
    // While doing this keep track of the original index and the city taken
    // A = 0 index, B = 1 index
    for i, vals := range costs {
        switch {  
        case vals[1] < vals[0]:
            taken[i] = []int{i, 1}
            to_b++
        default:
            taken[i] = []int{i, 0} 
            to_a++
        }
    }
    // Now we sort that 2d array based of the difference of its cost for A and B
    sort.Sort(byCityCost(taken))
    
    // No while A and B do not have the same number of people:   
    for i := 0; i < len(taken) && to_a != to_b; i++ {
        switch {
            // If A has more people then B takes the next (cheapest) swap            
            case to_a > to_b && taken[i][1] == 0:
                taken[i][1] = 1
                to_a--
                to_b++
            // Else if B has more people then A takes the next (cheapest) swap
            case to_b > to_a && taken[i][1] == 1:
                taken[i][1] = 0
                to_a++
                to_b--
        }
    }
    
    // finally we have our people and the city they are taking.
    // tally up their expenses
    result := 0
    for _, vals := range taken {
        result += costs[vals[0]][vals[1]]
    }    
    return result
}

func main() {
	input_1 := [][]int{{10,20},{30,200},{400,50},{30,20}}
	fmt.Println("Input 1:", input_1)
	fmt.Println("solution:", twoCitySchedCost(input_1))

	input_2 := [][]int{{10,20},{30,200},{400,401},{30,20}}
	fmt.Println("Input 2:", input_2)
	fmt.Println("solution:", twoCitySchedCost(input_2))
}