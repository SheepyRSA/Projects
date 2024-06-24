package com.varsitycollege.quickcal

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import kotlin.math.pow
import kotlin.math.sqrt


class MainActivity : AppCompatActivity() {
    var checkNumState: String = ""

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

//        The following was taken from the IIE Module manual to connect the layout to the main activity as well as the IF/When and While statements:
//        Author: The IIE. 2022. Introduction to Mobile App Dev [IMAD5112 Module Manual]. The Independent Institute of Education: Unpublished.

        val btnAdd = findViewById<Button>(R.id.btnAdd)
        val btnSub = findViewById<Button>(R.id.btnSub)
        val btnTimes = findViewById<Button>(R.id.btnTimes)
        val btnDev = findViewById<Button>(R.id.btnDev)
        val btnSquare = findViewById<Button>(R.id.btnSquare)
        val btnPow = findViewById<Button>(R.id.btnPow)
        val btnStat = findViewById<Button>(R.id.btnChangeView)
        val msgError = findViewById<TextView>(R.id.msgError)

        btnAdd?.setOnClickListener{
            checkNum()
            when (checkNumState) {
                "First" ->  msgError.text = "The first number missing"
                "Second"->  msgError.text = "The second number missing"
                "Both"  -> msgError.text = "Both numbers missing"
                else -> addNumbers()
            }
            checkNumState = ""
        }

        btnSub?.setOnClickListener{
            checkNum()
            when (checkNumState) {
                "First" ->  msgError.text = "The first number missing"
                "Second"->  msgError.text = "The second number missing"
                "Both"  -> msgError.text = "Both numbers missing"
                else -> subNumbers()

            }
            msgError.text = ""
            checkNumState = ""
        }

        btnTimes?.setOnClickListener{
            checkNum()
            when (checkNumState) {
                "First" ->  msgError.text = "The first number missing"
                "Second"->  msgError.text = "The second number missing"
                "Both"  -> msgError.text = "Both numbers missing"
                else -> mulNumbers()
            }
            checkNumState = ""
        }

        btnDev?.setOnClickListener{
            checkNum()
            when (checkNumState) {
                "First" ->  msgError.text = "The first number missing"
                "Second"->  msgError.text = "The second number missing"
                "Both"  -> msgError.text = "Both numbers missing"
                else -> divNumbers()
            }
            checkNumState = ""
        }

        btnSquare?.setOnClickListener{
            squareNumbers()
        }

        btnPow?.setOnClickListener {
            checkNum()
            when (checkNumState) {
                "First" ->  msgError.text = "The first number missing"
                "Second"->  msgError.text = "The second number missing"
                "Both"  -> msgError.text = "Both numbers missing"
                else -> powNumbers()
            }
            checkNumState = ""
        }

        btnStat?.setOnClickListener{
            val intent = Intent(this, StatFunctions::class.java)
            startActivity(intent)
        }
    }

//      The following methods on plus,minus, divide and multiplication was taken from Sololearn:
//      Author : Sololearn
//      Link : https://www.sololearn.com/learning/1160

    private fun checkNum() {
        val numX = findViewById<EditText>(R.id.etNumX)
        val numY = findViewById<EditText>(R.id.etNumY)
        var numXvar = numX.text.toString()
        var numYvar = numY.text.toString()

        while (numXvar == "" || numYvar == ""){
            if (numXvar == "" && numYvar == "") {
                checkNumState = "Both"
                numXvar = "0"
                numYvar = "0"
            }
            else if (numXvar == "") {
                numXvar = "0"
                checkNumState = "First"
            }
            else if (numYvar == "") {
                numYvar = "0"
                checkNumState = "Second"
            }
        }
    }

    private fun addNumbers() {
        val msgError = findViewById<TextView>(R.id.msgError)
        val numX = findViewById<EditText>(R.id.etNumX)
        val numY = findViewById<EditText>(R.id.etNumY)
        val msgCalc = findViewById<TextView>(R.id.msgCalc)
        var anw:Double = 0.0

        msgError.text = ""
        anw = numX.text.toString().toDouble() + numY.text.toString().toDouble()
        msgCalc.text = "${numX.text} + ${numY.text} = "+ anw}

    private fun subNumbers() {
        val msgError = findViewById<TextView>(R.id.msgError)
        val numX = findViewById<EditText>(R.id.etNumX)
        val numY = findViewById<EditText>(R.id.etNumY)
        val msgCalc = findViewById<TextView>(R.id.msgCalc)
        var anw:Double = 0.0

        msgError.text = ""
        anw = numX.text.toString().toDouble() - numY.text.toString().toDouble()
        msgCalc.text = "${numX.text} - ${numY.text} = "+ anw}

    private fun mulNumbers() {
        val msgError = findViewById<TextView>(R.id.msgError)
        val numX = findViewById<EditText>(R.id.etNumX)
        val numY = findViewById<EditText>(R.id.etNumY)
        val msgCalc = findViewById<TextView>(R.id.msgCalc)
        var anw:Double = 0.0

        msgError.text = ""
        anw = numX.text.toString().toDouble() * numY.text.toString().toDouble()
        msgCalc.text = "${numX.text} x ${numY.text} = "+ String.format("%.2f", anw).toDouble()}

    private fun divNumbers() {
        val msgError = findViewById<TextView>(R.id.msgError)
        val numX = findViewById<EditText>(R.id.etNumX)
        val numY = findViewById<EditText>(R.id.etNumY)
        val msgCalc = findViewById<TextView>(R.id.msgCalc)
        var anw:Double = 0.0

        var numYzero = numY.text.toString().toDouble()

        if (numYzero == 0.0){ msgError.text = "The second number cannot be zero" }
        else {msgError.text = ""
            anw = numX.text.toString().toDouble() / numY.text.toString().toDouble()
            msgCalc.text = "${numX.text} ÷ ${numY.text} = "+ String.format("%.2f", anw).toDouble()}}

//      The following methods on square root was taken from kotlinlang.org:
//      Author : Kotlin
//      Link : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.math/sqrt.html

    private fun squareNumbers() {
        val msgError = findViewById<TextView>(R.id.msgError)
        val numX = findViewById<EditText>(R.id.etNumX)
        val numY = findViewById<EditText>(R.id.etNumY)
        val msgCalc = findViewById<TextView>(R.id.msgCalc)
        var anw:Double = 0.0

        var numXzero = numX.text.toString()
        var numYblank = numY.text.toString()

        when {
            numXzero == "" -> {msgError.text ="First number required"}
            numXzero.toDouble() == 0.0 -> {msgError.text ="The first number cannot be 0 for the answer will be 0."}
            numYblank != "" -> {msgError.text ="No second number is required."}
            numXzero.toDouble() < 0.0 -> {
                anw = sqrt((numX.text.toString().toDouble()*-1))
                msgCalc.text = "sqrt(${numX.text}) =  "+ String.format("%.2f", anw).toDouble() + "i"
                msgError.text = "The first number cannot be below zero, thus an imaginary number (i)."}
            else -> {msgError.text = ""
                anw = sqrt(numX.text.toString().toDouble())
                msgCalc.text = "sqrt(${numX.text}) =  "+ String.format("%.2f", anw).toDouble()}
        }
    }
//              anw = numX.text.toString().toDouble().pow(1/numY.text.toString().toDouble())
//              msgCalc.text = "${numY.text}√${numX.text} =  "+ String.format("%.2f", anw).toDouble()}}

//      The following methods on power was taken from kotlinlang.org:
//      Author : Kotlin
//      Link : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.math/pow.html

    private fun powNumbers() {
        val msgError = findViewById<TextView>(R.id.msgError)
        val numX = findViewById<EditText>(R.id.etNumX)
        val numY = findViewById<EditText>(R.id.etNumY)
        val msgCalc = findViewById<TextView>(R.id.msgCalc)
        var firstNum = numX.text.toString().toDouble()
        var secNum = numY.text.toString().toInt()
        var x = 0
        var anw:Double = 1.0

        msgError.text = ""
        while (x < secNum) {
            anw *= firstNum
            x++
        }
        msgCalc.text = "${numX.text}^${numY.text} = " + anw}
//        anw = numX.text.toString().toDouble().pow(numY.text.toString().toDouble())
//        msgCalc.text = "${numX.text}^${numY.text} = " + String.format("%.2f", anw).toDouble()}

//      The following methods on functions was taken from Sololearn:
//      Author : Sololearn
//      Link : https://www.sololearn.com/learning/1160

}