import Excel from 'exceljs';
var convert = require('convert-units')

// const sheet = "country";
const filename = "./dataset_changed.xlsx";
const newFilename = "./dataset_changed_2.xlsx";

const workbook = new Excel.Workbook();
workbook.xlsx.readFile(filename)
    .then(function () {

        // uses col input B & output C
        const morphDataIntoIds = (sheet) => {

            const worksheet = workbook.getWorksheet(sheet);
            const col = worksheet.getColumn("B");
            const arr = [];
            let count = 1;
            col.eachCell((cell, rowNumber) => {
                if (rowNumber === 1) return;
                const idx = arr.findIndex((r) => r[0] === cell.value);
                if (idx !== -1) {
                    // already exists, replace value
                    worksheet.getRow(rowNumber).getCell("C").value = arr[idx][1];
                } else {
                    arr.push([
                        cell.value,
                        count
                    ]);
                    worksheet.getRow(rowNumber).getCell("C").value = count;
                    count++;
                }
                worksheet.getRow(rowNumber).commit();
            });


        };

        // Uses col input D & output E
        const removeDuplicatesAndUpdateRows = (sheet) => {
            const worksheet = workbook.getWorksheet(sheet);
            const col = worksheet.getColumn('D');
            const arr = [];
            let rowIndex = 2;
            col.eachCell((cell, rowNumber) => {
                    if (rowNumber === 1) return;
                    const idx = arr.findIndex(r => r[0] === cell.value);
                    if (idx !== -1) {
                        // already exists..
                        worksheet.getRow(rowNumber).getCell('E').value = "";
                    } else {
                        arr.push([
                            cell.value,
                            rowIndex
                        ]);
                        worksheet.getRow(rowIndex).getCell('E').value = cell.value;
                        rowIndex++;
                    }
                    worksheet.getRow(rowNumber).commit();
                }
            )
        };

        const thisAssignmentHasNothingToDoWithDatabases = (sheet) => {
            const worksheet = workbook.getWorksheet(sheet);
            const col = worksheet.getColumn("O");
            col.eachCell((cell, rowNumber) => {
                if (rowNumber === 1) return;
                if (!!cell.value || cell.value === null || cell.value === undefined) {
                    console.log("undefined..");
                    return;
                }
                const vals = cell.value.split('\'');
                const val = convert(vals[0]).from("in").to("cm") + convert(vals[1]).from("ft").to("cm")
                worksheet.getRow(rowNumber).getCell('O').value = val;
                worksheet.getRow(rowNumber).commit();
            })

        };

        thisAssignmentHasNothingToDoWithDatabases("player_stats");

        // morphDataIntoIds("body_type");

        // iterate over values, remove duplicates and update index

        // removeDuplicatesAndUpdateRows("country");
        // removeDuplicatesAndUpdateRows("club");
        // removeDuplicatesAndUpdateRows("body_type");


        workbook.xlsx.writeFile(newFilename)
            .then(() => console.log('done'))
    });