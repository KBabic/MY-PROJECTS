import { elements } from './base';

export const getInput = () => {
    const inputObj = {
        type: elements.inputType.value,
        description: elements.inputDescription.value,
        value: elements.inputValue.value
    };
    //console.log(inputObj);
    return inputObj;
}

const formatNumbers = (num) => {
    // numbers are: total income, total expenses, budget and every single income/expense
    // all of them are floats ==> first round them to 2 decimals
    num = num.toFixed(2);
    // 2570.80 ==> ['2570','80']
    // '2570' ==> '2' + ',' + '570'; '45300' ==> '45,300'
    // '2,570' + '80'
    const numArr = num.split('.');
    const int = numArr[0];
    const dec = numArr[1];
    let formatInt;
    if (int.length > 3) {
        formatInt = `${int.slice(0,int.length - 3)},${int.substr(1, int.length - 1)}`;
        num = `${formatInt}.${dec}`;
    } else {
        num = `${int}.${dec}`;
    }
    return num;

}

export const displayMonth = () => {
    const today = new Date();
    const year = today.getFullYear();
    const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    const month = months[today.getMonth()];
    elements.date.textContent = `${month}, ${year}`;
}

export const displayBudget = (totalInc, totalExp, budg, perc) =>  {
    // display total income:
    if (totalInc >=0 ) elements.totalIncome.textContent = formatNumbers(totalInc);
    // display total expenses:
    if (totalExp >=0 ) elements.totalExpense.textContent = formatNumbers(totalExp);
    // display total budget:
    if (budg >= 0) elements.totalBudget.textContent = formatNumbers(budg);
    // display percentage:
    if (perc) {
        elements.percentage.textContent = `${perc} %`;
    } else {
        elements.percentage.textContent = `---`;
    }
}

export const clearFields = () => {
    elements.inputDescription.value = "";
    elements.inputValue.value = "";
    elements.inputDescription.focus();
}

export const addIncomeList = (item) => {
    const markup = 
        `<div class="item clearfix" id="income-${item.id}">
            <div class="item__description">${item.description}</div>
            <div class="right clearfix">
                <div class="item__value">+ ${formatNumbers(item.value)}</div>
                <div class="item__delete">
                        <button class="item__delete--btn"><i class="ion-ios-close-outline"></i></button>
                </div>
            </div>
        </div>`;
    
    elements.incomesList.insertAdjacentHTML('beforeend',markup);

}

export const addExpenseList = (item) => {
    const markup =
    `<div class="item clearfix" id="expense-${item.id}">
        <div class="item__description">${item.description}</div>
        <div class="right clearfix">
            <div class="item__value">- ${formatNumbers(item.value)}</div>
            <div class="item__percentage">${item.percentage !== -1 ? item.percentage : '---' }</div>
            <div class="item__delete">
                <button class="item__delete--btn"><i class="ion-ios-close-outline"></i></button>
             </div>
        </div>
    </div>`;

    elements.expensesList.insertAdjacentHTML('beforeend', markup);
}

export const deleteIncome = (id) => {
    const inc = document.querySelector(`[id="income-${id}"]`);
    if (inc) inc.parentElement.removeChild(inc);
};

export const deleteExpense = (id) => {
    const exp = document.querySelector(`[id="expense-${id}"`);
    if (exp) exp.parentElement.removeChild(exp);
}
    


