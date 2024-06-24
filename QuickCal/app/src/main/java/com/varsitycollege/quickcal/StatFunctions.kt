package com.varsitycollege.quickcal

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import java.lang.reflect.Array
import java.util.*
import kotlin.collections.ArrayList

class StatFunctions : AppCompatActivity() {
    var numsToCalc = IntArray(10)
    var output = ""
    var a = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_stat_functions)

        val btnAddIn = findViewById<Button>(R.id.btnAddtoArray)
        val btnClear = findViewById<Button>(R.id.btnClearMem)
        val btnAvg = findViewById<Button>(R.id.btnAverage)
        val btnMinMax = findViewById<Button>(R.id.btnMinMax)
        val etArrayNum = findViewById<EditText>(R.id.etArrayNum)
        val tvStored = findViewById<TextView>(R.id.tvStoredNum)
        val tvAnswerDisp = findViewById<TextView>(R.id.tvAnswerDisp)
        var arrayCount = 0

//        The following was taken from the IIE Module manual to connect the layout to the main activity as well as the IF/When and While/FOR statements:
//        Author: The IIE. 2022. Introduction to Mobile App Dev [IMAD5112 Module Manual]. The Independent Institute of Education: Unpublished.

        btnAddIn?.setOnClickListener {
            var numArray = etArrayNum.text.toString()

            if (arrayCount >= 10){tvAnswerDisp.text = "Only up to 10 numbers can be added"}
            else if ( numArray.toInt() == 0){tvAnswerDisp.text = "You cannot put in a zero"}
            else if ( numArray != ""){
                addToArray()
                tvStored.text = output
                arrayCount += 1
            }
            else {tvAnswerDisp.text = "Numbers need to be added(up to 10)"}
            etArrayNum.text.clear()
        }

        btnClear?.setOnClickListener {
            numsToCalc = IntArray(10)
            tvStored.text = ""
            tvAnswerDisp.text = ""
            arrayCount -= arrayCount
            a -= a
            output = ""
        }

        btnAvg?.setOnClickListener {
            var arrayAvg = 0.0
            var arraySum = 0

            if (numsToCalc.sum() == 0){
                tvAnswerDisp.text = "Numbers required in the list"
            }
            else {
                tvAnswerDisp.text = ""
                for (i in numsToCalc) {
                   arraySum += i
                }
                arrayAvg = arraySum.toDouble() / arrayCount
                tvAnswerDisp.text = "The average is: " + String.format("%.2f", arrayAvg)
            }
        }

        btnMinMax?.setOnClickListener {
            var min = getMin()
            var max = getMax()

            if (numsToCalc.sum() == 0){
                tvAnswerDisp.text = "Numbers required in the list"
            }
            else { tvAnswerDisp.text = "The minimum is: $min and maximum is: $max"}
        }
    }

    private fun addToArray(){
        val etArrayNum = findViewById<EditText>(R.id.etArrayNum)
        var x = 0

        if (a < 10) {
            while (x < 1) {
                numsToCalc[a] = etArrayNum.text.toString().toInt()
                x++}
            output += "${numsToCalc[a]}; "
            a += 1
        }
    }

    private fun getMin(): Int {
        var lowestNum = numsToCalc[0]

        for (x in numsToCalc){
            if (x != 0) {
            if (x < lowestNum){
                lowestNum = x
                }
            }
        }
        return lowestNum
    }

    private fun getMax(): Int {
        var highestNum = numsToCalc[0]

        for (x in numsToCalc){
            if (x != 0) {
                if (x > highestNum){
                    highestNum = x
                }
            }
        }
        return highestNum
    }
}