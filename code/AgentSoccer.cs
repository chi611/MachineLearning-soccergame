using UnityEngine;
using Unity.MLAgents;
using Unity.MLAgents.Actuators;
using Unity.MLAgents.Policies;
/*
This work is based on https://github.com/Unity-Technologies/ml-agents, which is licensed under the Apache License, Version 2.0 (the "License").
A copy of the License is available at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

修改項目:
1.第175行的Heuristic函式。將
2.第62行新增playerTag變數。用來辨識第幾位球員
*/
public enum Team
{
    Blue = 0,
    Purple = 1
}

public class AgentSoccer : Agent
{
    // Note that that the detectable tags are different for the blue and purple teams. The order is
    // * ball
    // * own goal
    // * opposing goal
    // * wall
    // * own teammate
    // * opposing player

    public enum Position
    {
        Striker,
        Goalie,
        Generic
    }

    [HideInInspector]
    public Team team;
    float m_KickPower;
    // The coefficient for the reward for colliding with a ball. Set using curriculum.
    float m_BallTouch;
    public Position position;
    const float k_Power = 2000f;
    float m_Existential;
    float m_LateralSpeed;
    float m_ForwardSpeed;


    [HideInInspector]
    public Rigidbody agentRb;
    SoccerSettings m_SoccerSettings;
    BehaviorParameters m_BehaviorParameters;
    public Vector3 initialPos;
    public float rotSign;
    EnvironmentParameters m_ResetParams;

    public float playerTag;
    
    public override void Initialize()
    {
        SoccerEnvController envController = GetComponentInParent<SoccerEnvController>();
        if (envController != null)
        {
            m_Existential = 1f / envController.MaxEnvironmentSteps;
        }
        else
        {
            m_Existential = 1f / MaxStep;
        }

        m_BehaviorParameters = gameObject.GetComponent<BehaviorParameters>();
        if (m_BehaviorParameters.TeamId == (int)Team.Blue)
        {
            team = Team.Blue;
            initialPos = new Vector3(transform.position.x - 5f, .5f, transform.position.z);
            rotSign = 1f;
        }
        else
        {
            team = Team.Purple;
            initialPos = new Vector3(transform.position.x + 5f, .5f, transform.position.z);
            rotSign = -1f;
        }
        if (position == Position.Goalie)
        {
            m_LateralSpeed = 1.0f;
            m_ForwardSpeed = 1.0f;
        }
        else if (position == Position.Striker)
        {
            m_LateralSpeed = 0.3f;
            m_ForwardSpeed = 1.3f;
        }
        else
        {
            m_LateralSpeed = 0.3f;
            m_ForwardSpeed = 1.0f;
        }
        m_SoccerSettings = FindObjectOfType<SoccerSettings>();
        agentRb = GetComponent<Rigidbody>();
        agentRb.maxAngularVelocity = 500;

        m_ResetParams = Academy.Instance.EnvironmentParameters;
    }

    public void MoveAgent(ActionSegment<int> act)
    {
        var dirToGo = Vector3.zero;
        var rotateDir = Vector3.zero;

        m_KickPower = 0f;

        var forwardAxis = act[0];
        var rightAxis = act[1];
        var rotateAxis = act[2];

        switch (forwardAxis)
        {
            case 1:
                dirToGo = transform.forward * m_ForwardSpeed;
                m_KickPower = 1f;
                break;
            case 2:
                dirToGo = transform.forward * -m_ForwardSpeed;
                break;
        }

        switch (rightAxis)
        {
            case 1:
                dirToGo = transform.right * m_LateralSpeed;
                break;
            case 2:
                dirToGo = transform.right * -m_LateralSpeed;
                break;
        }

        switch (rotateAxis)
        {
            case 1:
                rotateDir = transform.up * -1f;
                break;
            case 2:
                rotateDir = transform.up * 1f;
                break;
        }

        transform.Rotate(rotateDir, Time.deltaTime * 100f);
        agentRb.AddForce(dirToGo * m_SoccerSettings.agentRunSpeed,
            ForceMode.VelocityChange);
    }

    public override void OnActionReceived(ActionBuffers actionBuffers)

    {

        if (position == Position.Goalie)
        {
            // Existential bonus for Goalies.
            AddReward(m_Existential);
        }
        else if (position == Position.Striker)
        {
            // Existential penalty for Strikers
            AddReward(-m_Existential);
        }
        MoveAgent(actionBuffers.DiscreteActions);
    }

    public override void Heuristic(in ActionBuffers actionsOut)
    {
        var discreteActionsOut = actionsOut.DiscreteActions;
        switch (playerTag){
            case 1:
                //forward
                if (Input.GetKey(KeyCode.Q))
                {
                    discreteActionsOut[0] = 1;
                }
                if (Input.GetKey(KeyCode.W))
                {
                    discreteActionsOut[0] = 2;
                }
                //right
                if (Input.GetKey(KeyCode.E))
                {
                    discreteActionsOut[1] = 1;
                }
                if (Input.GetKey(KeyCode.R))
                {
                    discreteActionsOut[1] = 2;
                }
            break;
            case 2:
                //forward
                if (Input.GetKey(KeyCode.A))
                {
                    discreteActionsOut[0] = 1;
                }
                if (Input.GetKey(KeyCode.S))
                {
                    discreteActionsOut[0] = 2;
                }
                //right
                if (Input.GetKey(KeyCode.D))
                {
                    discreteActionsOut[1] = 1;
                }
                if (Input.GetKey(KeyCode.F))
                {
                    discreteActionsOut[1] = 2;
                }
            break;
            case 3:
                //forward
                if (Input.GetKey(KeyCode.Z))
                {
                    discreteActionsOut[0] = 1;
                }
                if (Input.GetKey(KeyCode.X))
                {
                    discreteActionsOut[0] = 2;
                }
                //right
                if (Input.GetKey(KeyCode.C))
                {
                    discreteActionsOut[1] = 1;
                }
                if (Input.GetKey(KeyCode.V))
                {
                    discreteActionsOut[1] = 2;
                }
            break;
            case 4:
                //forward
                if (Input.GetKey(KeyCode.T))
                {
                    discreteActionsOut[0] = 1;
                }
                if (Input.GetKey(KeyCode.Y))
                {
                    discreteActionsOut[0] = 2;
                }
                //right
                if (Input.GetKey(KeyCode.U))
                {
                    discreteActionsOut[1] = 1;
                }
                if (Input.GetKey(KeyCode.I))
                {
                    discreteActionsOut[1] = 2;
                }
            break;                                    
        }

    }
    /// <summary>
    /// Used to provide a "kick" to the ball.
    /// </summary>
    void OnCollisionEnter(Collision c)
    {
        var force = k_Power * m_KickPower;
        if (position == Position.Goalie)
        {
            force = k_Power;
        }
        if (c.gameObject.CompareTag("ball"))
        {
            AddReward(.2f * m_BallTouch);
            var dir = c.contacts[0].point - transform.position;
            dir = dir.normalized;
            c.gameObject.GetComponent<Rigidbody>().AddForce(dir * force);
        }
    }

    public override void OnEpisodeBegin()
    {
        m_BallTouch = m_ResetParams.GetWithDefault("ball_touch", 0);
    }

}
