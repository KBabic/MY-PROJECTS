export default class Budget {
    constructor() {
        this.budgetData = {
            incomes: [],
            expenses: [],
            totalIncome: 0,
            totalExpenses: 0,
            totalPercentage: -1
        };
    }

    addItem (type, desc, val) {
        let inc, exp;
        if (type === 'income') {
            inc = {
                description: desc,
                value: parseFloat(val)
            };
            // id is always the id of the last element in incomes array increased by 1
            if (this.budgetData.incomes.length > 0) {
                inc.id = this.budgetData.incomes[this.budgetData.incomes.length - 1].id + 1;
            } else {
                inc.id = 0;
            }
            this.budgetData.incomes.push(inc);
            this.budgetData.totalIncome += inc.value;
            return inc;

        } else if (type === 'expense') {
            exp = {
                description: desc,
                value: parseFloat(val),
            };
             // id is always the id of the last element in expenses array increased by 1
            if (this.budgetData.expenses.length > 0) {
                exp.id = this.budgetData.expenses[this.budgetData.expenses.length - 1].id + 1;
            } else {
                exp.id = 0;
            }
            // if total income is > 0, calculate % of the current expense and add the % sign
            if (this.budgetData.totalIncome > 0) {
                exp.percentage = `${Math.round((exp.value / this.budgetData.totalIncome) * 100)}%`;
            } else {
                exp.percentage = -1;
            }
            this.budgetData.expenses.push(exp);
            this.budgetData.totalExpenses += exp.value;
            return exp;
        }
    }

    calculateBudget () {
        // budget = sum_of_incomes - sum_of_expenses
        this.budgetData.budget = this.budgetData.totalIncome - this.budgetData.totalExpenses;
        // if there is income, calculate total percentage of expenses:
        if (this.budgetData.totalIncome > 0) {
            this.budgetData.totalPercentage = Math.round((this.budgetData.totalExpenses / this.budgetData.totalIncome) * 100);
        }
        return [this.budgetData.totalIncome, this.budgetData.totalExpenses, this.budgetData.budget, this.budgetData.totalPercentage];
    }

    deleteItem (type, id) {
        if (type === 'income') {
            const arr = this.budgetData.incomes;
            const inc = arr.find(cur => cur.id == id);
            arr.splice(arr.findIndex(el => el === inc), 1);
            this.budgetData.totalIncome -= inc.value;
            return this.budgetData.incomes;
        } else if (type === 'expense') {
            const arr = this.budgetData.expenses;
            const exp = arr.find(cur => cur.id == id);
            arr.splice(arr.findIndex(el => el === exp), 1);
            this.budgetData.totalExpenses -= exp.value;
            return this.budgetData.expenses;
        }
    }
}