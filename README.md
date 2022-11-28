# 網路程式設計

## Lab 9 – Multicast

在所給定的範例程式中，multicast server S會不斷的送出 multicast 訊息，當 multicast client C 加入群組後即可接收到 S 所送出的訊息。

在這一個任務中，請寫一組轉發程式 BR 及 BC並改寫 S 與 C，BR 及 BC 的工作內容如下：

**BR:**
<ul>
    <li>程式執行時 BR 會加入 S 所在的 multicast group，並接收 S 所送出來的訊息</li>
    <li>BR 同時也扮演一個 Server 的角色，接受遠端Client BC 所送來的 TCP 連線要求，並將從 S 所收到的訊息轉送到 BC 中。</li>
</ul> 

**BC:**
<ul>
    <li>程式執行時 BC 會扮演TCP Client 的角色，從BR 中接收訊息</li>
    <li>BC 同時建立另一 multicast group，將從 BR 所接收到的訊息送到這一 multicast group，如此 multicast client C 加入這一 multicast 後就可以收到從 S 送出的訊息。</li>
</ul>  

S <-- multicast --> BR <-- tcp --> BC <-- multicast --> C

