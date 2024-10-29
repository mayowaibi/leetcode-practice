<h2><a href="https://www.lintcode.com/problem/920/description">Meeting Rooms</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an array of meeting time intervals consisting of start and end times, determine if a person could attend all meetings.</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> intervals = [(0,30),(5,10),(15,20)]
<strong>Output:</strong> false
<strong>Explanation:</strong>
(0,30), (5,10) and (0,30),(15,20) will conflict
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> intervals = [(5,8),(9,15)]
<strong>Output:</strong> true
<strong>Explanation:</strong>
Two times will not conflict
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= intervals.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= intervals[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><code>[(0,8), (8,10)]</code> will not conflict at 8.</li>
</ul>
