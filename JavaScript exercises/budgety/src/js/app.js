import Budget from './Budget';
import * as budgetView from './budgetView';
import { elements } from './base';

const budget = new Budget();

const init = () => {
    budgetView.displayMonth();
    window.addEventListener('load', budgetView.displayBudget(0, 0, 0));
}

init();


const ctrlAddItem = () => {
    // get input from the UI:
    const newInput = budgetView.getInput();
    // add item to the budget data:
    const newItem = budget.addItem(newInput.type, newInput.description, newInput.value);
    // calculate budget:
    const arrBudget = budget.calculateBudget();
    // add income/expense to the UI list:
    if (newInput.type === 'income') {
        //newItem.id = budget.budgetData.incomes.indexOf(newItem);
        budgetView.addIncomeList(newItem);
    } else if (newInput.type === 'expense') {
        //newItem.id = budget.budgetData.expenses.indexOf(newItem);
        budgetView.addExpenseList(newItem);
    }
    // display income, expenses and budget in the UI:
    budgetView.displayBudget(arrBudget[0], arrBudget[1], arrBudget[2], arrBudget[3]);
    budgetView.clearFields();
}
    
// Handle adding an item:
elements.addButton.addEventListener('click', ctrlAddItem);
document.addEventListener('keypress', e => {
    if (e.keyCode === 13 || e.which === 13) {
        ctrlAddItem();
    }     
});

// Handle deleting an income:
elements.incomesList.addEventListener('click', e => {
    // find the id of the element which is closest to where the click happened:
    const targetId = e.target.closest('.item').id;
    // handle the delete event:
    if (e.target.matches('.item__delete--btn, .item__delete--btn *')) {
        const id = targetId.split('-')[1];
        budget.deleteItem('income', parseInt(id, 10));
        budgetView.deleteIncome(id);
        const arrBudget = budget.calculateBudget();
        console.log(arrBudget);
        budgetView.displayBudget(arrBudget[0], arrBudget[1], arrBudget[2], arrBudget[3]);

    }

});

// Handle deleting an expense:
elements.expensesList.addEventListener('click', e => {
    const targetId = e.target.closest('.item').id;
    if (e.target.matches('.item__delete--btn, .item__delete--btn *')) {
        const id = targetId.split('-')[1];
        budget.deleteItem('expense', parseInt(id, 10));
        budgetView.deleteExpense(id);
        const arrBudget = budget.calculateBudget();
        console.log(arrBudget);
        budgetView.displayBudget(arrBudget[0], arrBudget[1], arrBudget[2], arrBudget[3]);
    }
});


